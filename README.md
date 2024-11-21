
# Machine Learning for 3D IC Floorplanning

## Repository Purpose

This repository supports research on evaluating machine learning (ML) optimization models for three-dimensional (3D) integrated circuit (IC) floorplanning. It aims to:

1. Train ML models to perform floorplanning for 3D ICs.
2. Compare ML-based models with traditional search-based floorplanners.
3. Evaluate models across metrics such as area, wirelength, temperature, and the number of through-silicon-vias (TSVs).

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
