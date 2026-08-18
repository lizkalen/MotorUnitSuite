- [HD-EMG Pipeline for Assessment in Spared Cortical Muscle Path Analysis](#hd-emg-pipeline-for-assessment-in-spared-cortical-muscle-path-analysis)
  - [Project Overview](#project-overview)
  - [1. Background and Motivation](#1-background-and-motivation)
    - [1.1 Clinical Need](#11-clinical-need)
    - [1.2 Current Assessment Limitations](#12-current-assessment-limitations)
    - [1.3 HD-EMG Advantages](#13-hd-emg-advantages)
  - [2. Literature Review](#2-literature-review)
    - [2.2 State-of-the-Art in HD-EMG Decoding](#22-state-of-the-art-in-hd-emg-decoding)
      - [2.2.1 Motor Unit Decomposition](#221-motor-unit-decomposition)
        - [**Blind Source Convolution and STUDY THIS IN DEPTH**](#blind-source-convolution-and-study-this-in-depth)
  - [**Motor Unit Tracking**](#motor-unit-tracking)
    - [2.3 Clinical Applications in SCI](#23-clinical-applications-in-sci)
  - [3. Problem Statement](#3-problem-statement)
  - [4. Methodology](#4-methodology)
    - [4.1 Hardware](#41-hardware)
    - [4.2 Data](#42-data)
    - [4.4 In Short](#44-in-short)
  - [Your Tasks Now](#your-tasks-now)
# HD-EMG Pipeline for Assessment in Spared Cortical Muscle Path Analysis

*Master Thesis Project Guide*

## Project Overview

This project aims to use HD-sEMG to improve current assessment and rehabilitation practices for patient with Stroke and Spinal Cord Injury

## 1. Background and Motivation

### 1.1 Clinical Need

Spinal cord injury affects approximately 17,000 new cases annually in the United States, with cervical injuries comprising 60% of cases. Accurate assessment of residual motor function is crucial for:

- **Treatment planning**: Tailoring rehabilitation strategies based on preserved pathways
- **Prognosis prediction**: Estimating recovery potential and functional outcomes
- **Intervention targeting**: Optimizing neural stimulation and assistive device selection
- **Progress monitoring**: Tracking changes in neural connectivity over time

### 1.2 Current Assessment Limitations

Traditional clinical assessments face several challenges:

- **Subjective scoring**: Manual muscle testing relies on clinician interpretation
- **Limited sensitivity**: Cannot detect subclinical motor unit activity
- **Binary classification**: Fails to capture gradual recovery patterns
- **Inter-rater variability**: Inconsistent assessments between clinicians

### 1.3 HD-EMG Advantages

High-density EMG offers significant improvements:

- **Motor unit resolution**: Individual motor unit action potential (MUAP) detection
- **Objective quantification**: Precise measurement of neural drive
- **Spatial information**: Muscle activation mapping through electrode arrays
- **Temporal dynamics**: Real-time assessment of motor unit recruitment

## 2. Literature Review

### 2.2 State-of-the-Art in HD-EMG Decoding

#### 2.2.1 Motor Unit Decomposition

**Start HERE:**

##### **Blind Source Convolution and STUDY THIS IN DEPTH**
- The beginning of HD-EMG decomposition
- Reliably detects motor units in HD-EMG data
- Verified against intramuscular EMG data
- Reference: [iopscience.iop.org/article/10.1088/1741-2560/13/2/026027](https://iopscience.iop.org/article/10.1088/1741-2560/13/2/026027/pdf)

**Then, look into recent advances and application in HD-EMG decomposition:**

**Motor Unit Tracking**
-
-
-

**Adaptive HD-sEMG Decomposition**
- Real-time motor unit decoding algorithm
- Adapts to signal non-stationarities from joint position and contraction changes
- Maintains high decoding accuracy across varying conditions
- Reference: PubMed 38479007

**Motor Unit based Real Time Control**
- Application of above's online deocomposition (non adaptive)
- First applications of Multi degree of freedom control 
- Evidence of unique motor units associated with specific movements

- Reference: [D.S Oliveira, Brain 2024](https://doi.org/10.1093/brain/awae088), [Yang 2025 BiorXiv](https://www.medrxiv.org/content/medrxiv/early/2025/12/13/2025.12.09.25341760.full.pdf)


### 2.3 Clinical Applications in SCI

Some additional information on how this is being investigated in clinical settings.

**High-density EMG in SCI Assessment**
- 150-electrode systems enable motor unit detection in complete motor paralysis
- Motor unit decomposition achieves 88±24% accuracy for real-time control
- EMG features strongly correlate with Fugl-Meyer scores (R² = 0.86)
- References: [Ting et al. (2021)](https://pubmed.ncbi.nlm.nih.gov/34788156/), [Tacca et al. (2026)](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=FsoRNXAAAAAJ&sortby=pubdate&citation_for_view=FsoRNXAAAAAJ:_kc_bZDykSQC)

## 3. Problem Statement

I'd rather discuss these in person than leave it written here, we can update the document together once we have chatted better.

## 4. Methodology

### 4.1 Hardware

At the moment we have a Ripple Neurotech based setup capable of rexording up to 32 channels simultaneously. We are working on procuring short term additional components to get to 64, and in the longer term an OTBio Quattrocento or toher system to go in the hundreds of channels.

### 4.2 Data

We have at the moment
- Data from a February Pilot test
- Data from two SCI Patients acquired in Erlagen 07/2026
- Data from 11 additional SCI patients, from the D.S. Oliveira paper cited above
- Simulation framework for trialling

### 4.4 In Short

We want to improve our EMG pipelin and apply it to study changes in Motor Unit Behaviour during the process of rehabilitation. Using the information extracted we additionally could try and correlate "microscopic" measurements of MU activity (e.g: firing rate, recruitment) to "macroscopic" measurements of therapeutical outcome (e.g: speed, coordination)

## Your Tasks Now

1. Dive more into the literature, using what I gave you as a starting point. Try to understand:
   1. What is actually being recorded?
   2. How is it being recorded?
   3. What do the different types of EMG algorithms do?

Then, we can chat.

**BEST OF LUCK!!!**
