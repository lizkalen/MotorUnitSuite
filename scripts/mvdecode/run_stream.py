"""Real-time streaming trial: feed the online run frame by frame against a wall clock
and report per-frame compute time and decision counts.

Reuses the fit + calibration from run_offline. Paths follow the same MVDEC_* env vars.

    python -u scripts/mvdecode/run_stream.py
"""
import os
import sys
import time
import pickle

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))                  # scripts/mvdecode -> repo root
sys.path.insert(0, os.path.join(REPO, "src"))                  # -> import mvdecoder

from mvdecoder import (EXPERLANGEN, TwoStageDecoder, StreamingDecoder,
                       TriggerStimSource, load_recording, load_feat_cache,
                       load_good_indices)

BASE = os.environ.get("MVDEC_BASE", r"D:\PatientGUI Output\experlangen")
ANALYSIS = os.environ.get("MVDEC_ANALYSIS", os.path.join(BASE, "analysis", "artifact_removal"))
ONLINE = os.environ.get("MVDEC_ONLINE",
                        os.path.join(BASE, "mv_Default-Training-Sequence_online_20260714_172405.raw"))
FRAME = int(os.environ.get("MVDEC_FRAME", "128"))          # device frame size (62.5 ms)
REALTIME = os.environ.get("MVDEC_REALTIME", "0") == "1"     # sleep to a wall clock?


def main():
    cfg = EXPERLANGEN
    good = load_good_indices(os.path.join(ANALYSIS, "good_mask.npy"))
    with open(os.path.join(BASE, "movement_model.pkl"), "rb") as f:
        trig_ch = int(pickle.load(f)["trig_ch"])
    tr = load_feat_cache(os.path.join(ANALYSIS, "feat_v2_stimtrain_parrm_good.npz"))
    dec = TwoStageDecoder(cfg, good).fit_from_cache(tr["F"], tr["A"], tr["E"], tr["gt"], tr["S"])

    data, trig, meta = load_recording(ONLINE, trig_ch=trig_ch)
    src = TriggerStimSource(trig_ch, cfg)
    thr, P = src.calibrate(trig)
    dec.set_calibration(thr, P)

    stream = StreamingDecoder(dec, src)
    budget_ms = FRAME / cfg.fs * 1000.0
    frame_ms, n_dec = [], 0
    N = data.shape[1]
    t0 = time.perf_counter()
    for k, s in enumerate(range(0, N, FRAME)):
        if REALTIME:
            due = t0 + (k + 1) * FRAME / cfg.fs
            while time.perf_counter() < due:
                pass
        a = time.perf_counter()
        evs = stream.process(data[:, s:s + FRAME])
        frame_ms.append((time.perf_counter() - a) * 1000.0)
        n_dec += len(evs)
    frame_ms = np.array(frame_ms)
    over = int((frame_ms > budget_ms).sum())
    print(f"frames: {len(frame_ms)} of {FRAME} samples (budget {budget_ms:.1f} ms)")
    print(f"compute/frame: mean {frame_ms.mean():.2f}  p95 {np.percentile(frame_ms, 95):.2f}  "
          f"max {frame_ms.max():.2f} ms   over budget: {over}")
    print(f"decisions emitted: {n_dec}")


if __name__ == "__main__":
    main()
