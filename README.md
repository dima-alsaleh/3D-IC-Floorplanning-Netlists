
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























# Data Collection and Refinement Process

## Overview

This section of the document provides a comprehensive explanation of the data collection process for our floorplanning netlist dataset. It includes a visual workflow, 
details on the sources used, and preprocessing steps, and how to run scripts, ensuring transparency and reproducibility.

---

## Data Collection Workflow

Below is a figure illustrating the steps involved in our data collection and data extraction processes:

![Data Collection and Extraction Schema](./additional%20ressources/data%20collection%20schema.png)

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
## External Resources and Dependencies for Replication

This repository requires several Python libraries to run the scripts. Below is a list of the libraries, their purpose, and installation instructions.

### Required Libraries




1. **Python**  
   - **Purpose**: The scripts in this repository require Python 3.x to run. Make sure you have Python installed.  
   - **Installation**:  
     - For installation instructions, visit the official Python website: [Download Python](https://www.python.org/downloads/)
     - Ensure Python 3.x is installed and added to your system’s PATH.


2. **requests**  
   - **Purpose**: Allows you to send HTTP requests, which is useful for interacting with web resources or APIs.  
   - **Installation**:  
     ```bash
     pip install requests
     ```
   - **Link**: [requests documentation](https://docs.python-requests.org/en/latest/)

3. **os**  
   - **Purpose**: Provides a way to interact with the operating system, allowing you to work with directories, files, and environment variables.  
   - **Installation**: This is part of Python’s standard library, so no installation is required.  
   - **Link**: [os module documentation](https://docs.python.org/3/library/os.html)

4. **argparse**  
   - **Purpose**: Used for parsing command-line arguments, which allows you to pass parameters when running the script from the terminal.  
   - **Installation**: This is part of Python’s standard library, so no installation is required.  
   - **Link**: [argparse documentation](https://docs.python.org/3/library/argparse.html)

5. **re**  
   - **Purpose**: Provides support for regular expressions in Python, allowing you to perform complex text searching and manipulation.  
   - **Installation**: This is part of Python’s standard library, so no installation is required.  
   - **Link**: [re module documentation](https://docs.python.org/3/library/re.html)

6. **random**  
   - **Purpose**: Implements pseudo-random number generators for various distributions, used for generating random numbers or selecting random elements.  
   - **Installation**: This is part of Python’s standard library, so no installation is required.  
   - **Link**: [random module documentation](https://docs.python.org/3/library/random.html)

7. **sys**  
    - **Purpose**: Provides access to system-specific parameters and functions, such as handling command-line arguments and interacting with the Python
     runtime environment.  
    - **Installation**: This is part of Python’s standard library, so no installation is required.  
    - **Link**: [sys module documentation](https://docs.python.org/3/library/sys.html)


8. **matplotlib**  
   - **Purpose**: A plotting library for creating static, animated, and interactive visualizations in Python.  
   - **Installation**:  
     ```bash
     pip install matplotlib
     ```
   - **Link**: [matplotlib documentation](https://matplotlib.org/)

9. **numpy**  
   - **Purpose**: A library for numerical computing in Python, providing support for large, multi-dimensional arrays and matrices, along with a large collection
    of high-level mathematical functions.  
   - **Installation**:  
     ```bash
     pip install numpy
     ```
   - **Link**: [numpy documentation](https://numpy.org/)

10. **pandas**  
   - **Purpose**: A library used for data manipulation and analysis, providing data structures like DataFrame for handling and analyzing data.  
   - **Installation**:  
     ```bash
     pip install pandas
     ```
   - **Link**: [pandas documentation](https://pandas.pydata.org/)

11. **shutil**  
   - **Purpose**: Provides a higher-level interface for file operations, including copying and removing files and directories.  
   - **Installation**: This is part of Python’s standard library, so no installation is required.  
   - **Link**: [shutil module documentation](https://docs.python.org/3/library/shutil.html)

### Installation Instructions

To set up the environment for this repository, again please ensure you have Python 3.x installed and properly added to your system's PATH. 
Then, you can install the necessary dependencies
 using `pip` by running the following command:


pip install <library_name>>



## Notes on Limitations

While the data collection process prioritized quality and comprehensiveness, certain limitations must be noted:
- The dataset reflects only publicly accessible netlists from the identified sources and may exclude proprietary or confidential industry designs.
- Sampling is limited to files available as of **November 20, 2024**.
- Variability in the level of detail across sources (e.g., GitHub repositories) may affect uniformity.

