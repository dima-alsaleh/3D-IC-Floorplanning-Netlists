
# Machine Learning for 3D IC Floorplanning

## Repository Purpose

This repository supports research on evaluating machine learning (ML) optimization models for three-dimensional (3D) integrated circuit (IC) floorplanning. 
The goal is to advance the field of 3D IC design by exploring the potential of ML models in solving complex floorplanning problems and comparing their effectiveness against traditional search-based approaches.

Specifically, the repository aims to:
1. Train ML models to perform floorplanning for 3D ICs. The model should be capable of generating optimized floorplans for 3D ICs. To train the model a dataset is required.
2. Compare the performance and quality of output of ML-based models with traditional search-based floorplanners on various circuits.
3. Train and assess the effectiveness of ML models in optimizing key metrics that significantly influence 3D IC performance and manufacturability:

    Area: Minimize the overall footprint of the design to conserve chip space.
    Wirelength: Reduce the total length of interconnects to communication delays.
    Temperature: Achieve optimal thermal distribution to prevent hotspots and ensure long-term reliability.
    Through-Silicon-Vias (TSVs): Minimize the number of TSVs to lower costs and decrease communication delays.


Therefore, to train, test, and compare ML models we require a dataset of netlists with industry significance.
These netlists can include dimensions of circuit components (or blocks) for area optimization, connections between blocks for wirelength and number of TSVs optimization, and power requirements 
of blocks for thermal optimization. Thus the dataset obtained is simply a collection of netlists of various circuits with details regarding the components of these circuits.

The collected netlists vary in the type and completeness of data they provide. Some netlists include a subset of these attributes, focusing on specific aspects such as 
dimensions or connections, while others provide all the required details, enabling a more holistic approach to optimization. These variations reflect the diversity of design 
challenges and application-specific needs within the industry, ensuring the dataset is robust and representative of real-world scenarios.
Additional information regarding the purpose of the repository can be found in [Research Question PDF](./additional%20ressources/research%20question.pdf) and in 
[Study Design PDF](./additional%20ressources/study%20design.pdf)


## Data Sources

The raw data comprises IC netlists from reliable and publicly accessible platforms, including:

- **GitHub**: Various IC netlist repositories from industry players and researchers.
- **Southern Methodist University (SMU) Platform**: Benchmarks from the Microelectronics Center of North Carolina (MCNC).
- **University of Michigan (UM) Platform**: VLSI netlists, including official IBM netlists.

## Repository Structure

### 1. `raw_data/`

Contains unprocessed IC netlists retrieved from the identified data sources. 

- **Subdirectories**: 
  - `github/`: Netlists from GitHub repositories.
  - `smu/`: Netlists from the SMU platform.
  - `um/`: Netlists from the UM platform.

### 2. `scripts/`

Includes all scripts for data handling and preprocessing.

- `data_download.py`: Automates the retrieval of data from GitHub.
- `preprocess_netlists.py`: Standardizes netlists by format and units.
- `duplicate_removal.py`: Detects and removes duplicate netlists.
- `data_augmentation.py` (optional): Expands data by generating new netlists based on existing ones.

### 3. `processed_data/`

Contains the cleaned and standardized netlists ready for ML model training.

- **Files**:
  - `block_specs.csv`: Specifications for each block in micrometers.
  - `block_connectivity.csv`: Describes block-to-block connections.
  - `power_requirements.csv` (optional): Power requirements for blocks.

### 4. `statistics/`

Holds summaries and visualizations describing the processed dataset.

- `dataset_summary.txt`: Overview of dataset metrics (e.g., total netlists, average dimensions, block connectivity).
- `visualizations/`: Charts and graphs of key metrics.

## Key Processes

1. **Data Retrieval**:
   - GitHub data is downloaded using automated scripts.
   - SMU and UM data are manually downloaded due to API limitations.

2. **Data Preprocessing**:
   - Formats and units are standardized for consistency.
   - Duplicate netlists are removed to ensure unbiased training.

3. **Optional Data Augmentation**:
   - New netlists are synthesized by altering connectivity while preserving original properties.

## Notes

- The repository primarily serves researchers and practitioners in ML and IC design.
- Detailed documentation for each script and dataset is available in the respective directories.

For further details, refer to the included research proposal or contact the repository maintainer.























# Data Collection Process

## Overview

This document provides a comprehensive explanation of the data collection process for our floorplanning netlist dataset. It includes a visual workflow, details on the sources used, and preprocessing steps, ensuring transparency and reproducibility.

---

## Data Collection Workflow

Below is a figure illustrating the steps involved in our data collection process:

![Data Collection Process](figures/figure.png)

---

## Detailed Explanation of the Workflow

### 1. Define Objectives
   - The dataset is collected to train machine learning models for 3D integrated circuit (IC) floorplanning.
   - Key variables include block specifications (e.g., dimensions, connectivity) and metadata such as power consumption.
   - Focus areas include optimizing area, wirelength, temperature, and through-silicon-vias (TSVs).

### 2. Source Identification
   - **Southern Methodist University (SMU) Platform**:
     - Hosts benchmark netlists and circuits commonly used in academic and industry floorplanning research.
   - **University of Michigan (UM) Platform**:
     - Provides benchmark netlists for very-large-scale integration (VLSI) design, frequently referenced in 3D IC research.
   - **GitHub Repositories**:
     - A variety of repositories with IC netlists, including those shared by major players such as Google DeepMind.

### 3. Data Download Steps
   - **SMU Platform**:
     1. Access the SMU Platform at https://s2.smu.edu/~manikas/.
     2. Navigate to "Benchmark netlists and circuits."
     3. Download the **MCNC Benchmark Netlists** (8 files relevant to block netlists for 3D IC floorplanning).
   - **UM Platform**:
     1. Visit the UM Platform at http://vlsicad.eecs.umich.edu/BK/CompaSS/results/gsrc_soft.html.
     2. Download relevant benchmark netlists for VLSI design.
   - **GitHub**:
     - Perform a targeted query for IC netlists and manually review repositories for quality and relevance.
     - Use Python scripts to automate the downloading process for selected repositories.

### 4. Preprocessing
   - **Cleaning**:
     - Standardization of formats (e.g., uniform units for dimensions such as micrometers).
     - Removal of duplicate netlists to prevent bias in training.
   - **Software**:
     - Scripts written in Python using libraries like Pandas handled the majority of preprocessing.

### 5. Data Validation
   - **Methods**:
     - Consistency checks for file integrity and completeness.
     - Validation of block specifications and connectivity data against benchmarks.
   - **Statistical Checks**:
     - Verification of block dimensions, power values, and connectivity structure for anomalies.

---

## Notes on Limitations

While the data collection process prioritized quality and comprehensiveness, certain limitations must be noted:
- The dataset reflects only publicly accessible netlists from the identified sources and may exclude proprietary or confidential industry designs.
- Sampling is limited to files available as of **November 20, 2024**.
- Variability in the level of detail across sources (e.g., GitHub repositories) may affect uniformity.

