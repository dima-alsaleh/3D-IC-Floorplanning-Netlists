
# Machine Learning for 3D IC Floorplanning

## Repository Purpose

This repository supports research on evaluating machine learning (ML) optimization models for three-dimensional (3D) integrated circuit (IC) floorplanning. 
The goal is to advance the field of 3D IC design by exploring the potential of ML models in solving complex floorplanning problems and comparing their effectiveness against traditional search-based approaches.

Specifically, the repository aims to:
1. Train ML models to perform floorplanning for 3D ICs. The model should be capable of generating optimized floorplans for 3D ICs. To train the model, a dataset is required.
2. Compare the performance and quality of output of ML-based models with traditional search-based floorplanners on various circuits.
3. Train and assess the effectiveness of ML models in optimizing key metrics that significantly influence 3D IC performance and manufacturability:

    Area: Minimize the overall footprint of the design to conserve chip space.
    Wirelength: Reduce the total length of interconnects to minimize communication delays.
    Temperature: Achieve optimal thermal distribution to prevent hotspots and ensure long-term reliability.
    Through-Silicon-Vias (TSVs): Minimize the number of TSVs to lower costs and decrease communication delays.


Therefore, to train, test, and compare ML models, we require a dataset of netlists with industry significance.
These netlists can include dimensions of circuit components (or blocks) for area optimization, connections between blocks for wirelength and number of TSVs optimization, and power requirements of blocks for thermal optimization. Thus the dataset obtained is simply a collection of netlists of various circuits with details regarding the components of these circuits.

The collected netlists vary in the type and completeness of data they provide. Some netlists include a subset of these attributes, focusing on specific aspects such as 
dimensions or connections, while others provide all the required details, enabling a more holistic approach to optimization. These variations reflect the diversity of design 
challenges and application-specific needs within the industry, ensuring the dataset is robust and representative of real-world scenarios.
Additional information regarding the purpose of the repository can be found in [Research Question PDF](./additional%20resources/research%20question.pdf) and in 
[Study Design PDF](./additional%20resources/study%20design.pdf)


## Repository Structure

### 1. `raw data/`

Contains unprocessed IC netlists retrieved from the identified data sources. 

- **Subdirectories**: 
  - `Corblivar/`: Netlists from the Corblivar repository on Github, https://github.com/DfX-NYUAD/Corblivar/tree/master/exp/benches, accessed on November 20, 2024.
  
  - `DeepMind/`: Netlists from the DeepMind repository on Github,  https://github.com/google-research/circuit_training/blob/main/circuit_training/environment/test_data/simple_with_coords/netlist.pb.txt, accessed on November 20,2024.
  
  - `HotSpot/`: Netlists from the HotSpot repository on Github, https://github.com/uvahotspot/HotSpot/tree/master/examples/example6, accessed on November 20, 2024.

  - `SMU/`: Netlists from the SMU platform. https://s2.smu.edu/~manikas/Benchmarks/MCNC_Benchmark_Netlists.html, , accessed on November 19, 2024.

  - `UM/`: Netlists from the UM platform. http://vlsicad.eecs.umich.edu/BK/CompaSS/results/gsrc_soft.html  accessed on November 19, 2024.


  The raw netlists are provided in their various original formats (e.g., .txt, .nets). Formats were determined through reviewing associated documentation, including README files and posted explanations on their respective links.


### 2. `scripts/`

This directory includes all scripts required for data management, cleaning, statistical analysis, and augmentation.

- **Subdirectories**: 
  - `data_collection_scripts`: Scripts that automate the retrieval of data from GitHub (i.e., Corblivar, Hotspot, and DeepMind).
  - `data_extraction_scripts`: Scripts that standardize netlists by format and units for each data source.
- `remove_duplicates.py`: Detects duplicate netlists and removes them to improve data quality.
- `generate_statistics_extracted_data.py`: Statistically analyzes the netlists without duplicates and generates relevant figures.
- `data_augmentation.py` (optional): Expands data by generating new netlists based on existing ones.

### 3. `refined data/`
Contains processed IC netlists that have been standardized for consistency across all data sources. This folder has two subdirectories:

- **Subdirectories**:
  - `extracted data with duplicates/`:  
    This subdirectory contains five folders, each corresponding to one of the original data sources. The netlists in these folders have been standardized into a common format for ease of analysis. The folders are structured as follows:
    - `UM_netlists/`: Contains standardized netlists originally retrieved from the UM platform.
    - `SMU_netlists/`: Contains standardized netlists originally retrieved from the SMU platform.
    - `HotSpot_netlists/`: Contains standardized netlists originally retrieved from the HotSpot repository.
    - `DeepMind_netlists/`: Contains standardized netlists originally retrieved from the DeepMind repository.
    - `Corblivar_netlists/`: Contains standardized netlists originally retrieved from the Corblivar repository.
    Note: Some netlists in the raw data were not standardized because they contained both soft and hard blocks. Soft blocks, which lack fixed dimensions, fall outside the scope of this work.

  - `extracted data without duplicates/`:  
    This subdirectory consolidates all standardized netlists from the five sources into a single folder. Duplicates have been removed to ensure unique entries, facilitating clean analysis and comparison.

- **How to Read standardized Files**

  The standardized netlists across both subdirectories follow a unified structure and format, designed to be machine-readable and user-friendly. Each file is encoded as a plain-text `.txt` file. Moreover, the standardized netlists are formatted to be consistent and machine-readable. Each file is divided into two sections: `Blocks` and `Connections`.

  - **Blocks Section**:

  This section lists all blocks in the circuit, each defined by the following attributes:  
  - **Name**: The unique identifier for the block (e.g., `Icache`, `Dcache`, `blk5`).  
  - **Width (µm)**: The width of the block in micrometers.  
  - **Height (µm)**: The height of the block in micrometers.  
  - **Power (W)**: The power consumption of the block in watts. If this data is unavailable in the original raw data, the value is recorded as `None`.  



  - **Connections Section**:  
  Details the connections (nets) between blocks and terminals, if any. Each net includes:  
    - **Net Identifier**: Unique name for the net.  
    - **Blocks and Terminals**: List of blocks and terminals associated with the net.

  

### 4. `statistics of refined data/`
Holds a statistical summary of the extracted data without duplicates and visualizations describing the various netlists. All files in this folder were generated using the script generate_statistics_extracted_data.py


### 5. `augmented data/`
Holds additional artificially generated netlists. These netlists were generated based on the extracted statistics, properties and characteristics extracted during the statistical analysis process.Therefore, even though they are generated they remain consistent with the industry standards.
### 6. `additional resources/`

Holds additional documentation and resources like the study design and research questions.

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
- For further details, refer to the included research proposal or contact the repository maintainer dima.alsaleh@mail.mcgill.ca.



# Data Collection and Refinement Process

## Overview

This section of the document provides a comprehensive explanation of the data collection and refinement process for our floorplanning netlist dataset. It includes a visual workflow, details on the sources used, preprocessing steps, and how to run scripts, ensuring transparency and reproducibility.

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



## Data Collection Workflow

Below is a figure illustrating the steps involved in our data collection and data extraction processes:

![Data Collection and Extraction Schema](./additional%20resources/data%20collection%20schema.png)

---

## Detailed Explanation of the Workflow

### 1. Define Objectives
   - The dataset is collected to train machine learning models for 3D integrated circuit (IC) floorplanning.
   - Key variables include block specifications (e.g., dimensions, connectivity, and power).
   - The goal is to optimize area, wirelength, temperature, and through-silicon-vias (TSVs).

### 2. Source Identification
After manual selection using snowballing techniques, the below sources were identified.
   - **Southern Methodist University (SMU) Platform**:
     - Hosts benchmark netlists and circuits commonly used in academic and industry floorplanning research, accessed on November 19, 2024. https://s2.smu.edu/~manikas/Benchmarks/MCNC_Benchmark_Netlists.html 
   - **University of Michigan (UM) Platform**:
     - Provides benchmark netlists for very-large-scale integration (VLSI) design, frequently referenced in 3D IC research, accessed on November 19, 2024. http://vlsicad.eecs.umich.edu/BK/CompaSS/results/gsrc_soft.html
   - **GitHub Repositories**:
     - A variety of repositories with IC netlists, including those shared by major players such as Google DeepMind. More specifically, the following repositories on Github were selected:
        - Corblivar  https://github.com/DfX-NYUAD/Corblivar/tree/master/exp/benches, accessed on November 20, 2024.
        - HotSpot https://github.com/uvahotspot/HotSpot/tree/master/examples/example6, accessed on November 20, 2024.
        - DeepMind https://github.com/google-research/circuit_training/blob/main/circuit_training/environment/test_data/simple_with_coords/netlist.pb.txt, accessed on November 20,2024.


These sources were identified through a process of snowballing. The papers referencing those citations are available in [Study Design PDF](./additional%20resources/study%20design.pdf)



### 3. Data Download Steps
To download the files of the raw dataset, please follow the below steps. 
   - **SMU Platform**: 
     1. Access the SMU Platform at https://s2.smu.edu/~manikas/.
     2. Navigate to "Benchmark netlists and circuits" at the bottom of the page.
     3. Click on the **MCNC Benchmark Netlists**.
     4. Download the block netlists (8 files relevant to block netlists for 3D IC floorplanning) by clicking on the links under the phrase "Often used to test floorplanning methods.".

   - **UM Platform**:
     1. Visit the UM Platform at http://vlsicad.eecs.umich.edu/BK/CompaSS/results/gsrc_soft.html.
     2. Download all 12 files available on that page (3 files for n100, 3 files for n200, 3 files for n300, and 3 files for n600).

   - **GitHub Corblivar**:
     1. In the terminal, navigate to the path where the scripts for data collection are saved:  
     [Scripts for Data Collection](scripts/data_collection_scripts/)
     2. Run the following command:  
     ```bash
     python download_files_corblivar.py <output_directory>
     ```
     But, replace <output_directory> with the desired location where the files should be saved.  
        - If the output directory path contains spaces, enclose it in double quotes (`"`).  
          For example:  
          ```bash
          python download_files_corblivar.py "path/with spaces/output_directory"
          ``` 
  - **GitHub DeepMind**:
     1. In the terminal, navigate to the path where the scripts for data collection are saved:  
     [Scripts for Data Collection](scripts/data_collection_scripts/)
     2. Run the following command:  
     ```bash
     python download_files_deepmind.py <output_directory>
     ```
     But, replace <output_directory> with the desired location where the files should be saved.  
        - If the output directory path contains spaces, enclose it in double quotes (`"`).  
          For example:  
          ```bash
          python download_files_deepmind.py "path/with spaces/output_directory"
          ```
  - **GitHub HotSpot**:
     1. In the terminal, navigate to the path where the scripts for data collection are saved:  
     [Scripts for Data Collection](scripts/data_collection_scripts/)
     2. Run the following command:  
     ```bash
     python download_files_hotspot.py <output_directory>
     ```
     But, replace <output_directory> with the desired location where the files should be saved.  
        - If the output directory path contains spaces, enclose it in double quotes (`"`).  
          For example:  
          ```bash
          python download_files_hotspot.py "path/with spaces/output_directory"
          ```

### 4. Data refinement steps
Data refinement consists of two main steps, data uniformization and duplicate removal. 
The first step, data uniformization, is essential to guarantee that netlists are standardized and can easily be read and interpreted.
In this step, the name of the block, along with width and height of each block in micrometers (µm) are extracted. If the power requirement of the block is provided, it is also extracted,
along with the connections various blocks have amongst one another.
This extracted data from the raw data is then written in the standardized netlists in a consistent way. 
To complete data uniformization you need to follow the below steps. 


  - **SMU data uniformization**: 
     1. In the terminal, navigate to the path where the scripts for data extraction are saved:  
     [Scripts for Data Extraction](scripts/data_extraction_scripts/)
     2. Run the following command:  
     ```bash
     python extract_SMU_netlists.py <input_directory> <output_directory>
     ```
     But, replace <input_directory> with the path where the raw data from SMU was saved.
     And replace <output_directory> with the desired location where the files should be saved.  
        - If the input or output directory path contains spaces, enclose it in double quotes (`"`).  
          For example:  
          ```bash
          python extract_SMU_netlists.py "path/with spaces/input_directory" "path/with spaces/output_directory"
          ``` 

  - **UM data uniformization**:
     1. In the terminal, navigate to the path where the scripts for data extraction are saved:  
     [Scripts for Data Extraction](scripts/data_extraction_scripts/)
     2. Run the following command:  
     ```bash
     python extract_UM_netlists.py <input_directory> <output_directory>
     ```
     But, replace <input_directory> with the path where the raw data from UM was saved.
     And replace <output_directory> with the desired location where the files should be saved. 
        - If the input or output directory path contains spaces, enclose it in double quotes (`"`).  
          For example:  
          ```bash
          python extract_UM_netlists.py "path/with spaces/input_directory" "path/with spaces/output_directory"
          ``` 

  - **Corblivar data uniformization**:
     1. In the terminal, navigate to the path where the scripts for data extraction are saved:  
     [Scripts for Data Extraction](scripts/data_extraction_scripts/)
     2. Run the following command:  
     ```bash
     python extract_Corblivar_netlists.py <input_directory> <output_directory>
     ```
     But, replace <input_directory> with the path where the raw data from Corblivar was saved. 
     And replace <output_directory> with the desired location where the files should be saved. 
     
        - If the input or output directory path contains spaces, enclose it in double quotes (`"`).  
          For example:  
          ```bash
          python extract_Corblivar_netlists.py "path/with spaces/input_directory" "path/with spaces/output_directory"
          ``` 
  - **DeepMind data uniformization**:
     1. In the terminal, navigate to the path where the scripts for data extraction are saved:  
     [Scripts for Data Extraction](scripts/data_extraction_scripts/)
     2. Run the following command:  
     ```bash
     python extract_DeepMind_netlists.py <input_directory> <output_directory>
     ```
     But, replace <input_directory> with the path where the raw data from DeepMind was saved.
     And replace <output_directory> with the desired location where the files should be saved.  
        - If the input or output directory path contains spaces, enclose it in double quotes (`"`).  
          For example:  
          ```bash
          python extract_DeepMind_netlists.py "path/with spaces/input_directory" "path/with spaces/output_directory"
          ```
  - **HotSpot data uniformization**:
     1. In the terminal, navigate to the path where the scripts for data extraction are saved:  
     [Scripts for Data Extraction](scripts/data_extraction_scripts)
     2. Run the following command:  
     ```bash
     python extract_HotSpot_netlists.py <input_directory> <output_directory>
     ```
     But, replace <input_directory> with the path where the raw data from HotSpot was saved.  
     And replace <output_directory> with the desired location where the files should be saved.
        - If the input or output directory path contains spaces, enclose it in double quotes (`"`).  
          For example:  
          ```bash
          python extract_HotSpot_netlists.py "path/with spaces/input_directory" "path/with spaces/output_directory"
          ```


  - **Duplicates removal**:
     - Since the downloaded raw data originated from multiple sources, duplicates are likely to be present.
      After standardization of formats it becomes easy to determine which netlists are duplicates.
      Removing duplicates is essential to avoid overtraining the ML model on a certain circuit, it also permits data analysis
      and statistical analysis of the extracted data. 

      To remove duplicates please follow the steps below. 
        - **Steps for removing duplicates**:
          1. In the terminal, navigate to the path where the script for removing duplicates is saved: [Scripts for Removing Duplicates](scripts)
          2. Run the following command:  
          ```bash
          python remove_duplicates.py <input_directory> <output_directory>
          ```
          But, replace <input_directory> with the path where the folders containing uniformed netlists based on each source, can be found. In this repository the input path corresponds to  [Extracted Data with Duplicates](./refined%20data/extracted%20data%20with%20duplicates/).
          And replace <output_directory> with the desired location where the files should be saved.
              - If the input or output directory path contains spaces, enclose it in double quotes (`"`).  
                For example:  
                ```bash
                python remove_duplicates.py "path/with spaces/input_directory" "path/with spaces/output_directory"
                ```

### 5. Statistics regarding Refined Data
  This step is essential to identify patterns in our data and identify what typical charactersistics of netlists from the industry are. 
  This will also allow data augmentation.
   - **How to reproduce statistical output**:
          1. In the terminal, navigate to the path where the script for statistical analysis is saved:  
             [Scripts for Statistics](scripts)
          2. Run the following command:  
          ```bash
          python generate_statistics_extracted_data.py <input_directory> <output_directory>
          ```
          But, replace <input_directory> with the path where the netlists without duplicates were saved. This essentially corresponds to the output path of the previous step (duplicate removal). In this repository the input path for this step corresponds to  [Extracted Data without Duplicates](./refined%20data/extracted%20data%20without%20duplicates/)
          And replace <output_directory> with the desired location where the files should be saved. We decided to save at [Statistics Refined Data](./statistics%20of%20refined%20data/).
              - If the input or output directory path contains spaces, enclose it in double quotes (`"`).  
                For example:  
                ```bash
                python generate_statistics_extracted_data.py "path/with spaces/input_directory" "path/with spaces/output_directory"
                ```
   - **Statistical Analysis**:
     - We notice that all netlists share some patterns in terms of number of connections per blocks, power requirement, width and aspect ratio, even though netlists were designed by different industry players. 
     - Results from Statistical Analysis
         Below a brief statistical description of the collected data is offered, for further information, please do not hesitate to contact the repository manager dima.alsaleh@mail.mcgill.ca or to review the figures in the [`statistics refined data`](./statistics%20of%20refined%20data/) directory.

        * Overview
        The netlists exhibit common patterns across several parameters, including the number of connections per block, power requirements, widths, and aspect ratios, despite being designed by different industry players. Below is a detailed statistical analysis based on the provided data.

       * Aspect Ratio
        - **Histogram Analysis**:
          - The aspect ratio distribution is right-skewed, with the majority of values concentrated below 2.
          - A significant number of blocks have an aspect ratio close to 1, which indicates nearly square layouts are prevalent.
          - Outliers with aspect ratios greater than 3 are rare, but they exist.

        - **Descriptive Statistics**:
          - **Average**: 1.22  
          - **Median**: 1.00  
          - **1st Quartile (Q1)**: 0.68  
          - **3rd Quartile (Q3)**: 1.54  

        * Connection Counts
        - **Box Plot Analysis**:
          - The distribution of connection counts is heavily skewed with a dense cluster of blocks having fewer than 20 connections.
          - There are notable outliers with connection counts exceeding 40 and reaching up to 100, suggesting a small subset of highly connected blocks.

        * Width
        - **Descriptive Statistics**:
          - **Average**: 132.17  
          - **Median**: 34.00  
          - **1st Quartile (Q1)**: 23.00  
          - **3rd Quartile (Q3)**: 44.00  

          The widths show significant variability, with most blocks having widths between 23 and 44 units, but with some outliers extending beyond these ranges.

        * Power Requirements
        - **Descriptive Statistics**:
          - **Average**: 0.46  
          - **Median**: 0.02  
          - **1st Quartile (Q1)**: 0.01  
          - **3rd Quartile (Q3)**: 0.07  

          The power requirement data suggest that most blocks consume minimal power (close to 0.02 on average), with a few higher-power outliers inflating the mean.

        * Key Observations:
        - **Correlation Across Parameters**:
          - The analysis highlights patterns such as compact designs (aspect ratio ~1) and lower power usage for most blocks, aligning with industry practices for efficient layouts.
          - Outliers in connection counts, widths, and power requirements may indicate specialized blocks or unique design needs.

        * Industry Design Trends**:
          - Despite differences in design origins, the overall patterns suggest shared optimization objectives, particularly in reducing area and power while managing connectivity complexity.




### 6. Data Augmentation
Due to the limited amount of netlists, we propose to improve training of the model by using data augmentation.
Although this step remains optional, we provided the script for data augmentation and created 50 example netlists, based on the properties extracted during the statistical analysis of reputable netlists.
- **How to**:
   1. In the terminal, navigate to the path where the script for data augmentation is saved:  
             [Scripts for Data Augmentation](scripts)
          2. Run the following command:  
          ```bash
          python data_augmentation.py  <output_directory>
          ```
          But, replace <output_directory> with the desired location where the files should be saved. We decided to save the generated netlists at [Augmented Data](augmented%20data/).
              - If the output directory path contains spaces, enclose it in double quotes (`"`).  
                For example:  
                ```bash
                python data_augmentation.py  "path/with spaces/output_directory"
                ```

---




## Notes on Limitations

While the data collection process prioritized quality and comprehensiveness, certain limitations must be noted:
- The dataset reflects only publicly accessible netlists from the identified sources and may exclude proprietary or confidential industry designs.
- Sampling is limited to files available as of November 20, 2024.
- Variability in the level of detail across sources (e.g., GitHub repositories) may affect uniformity.
- Data augmentation is proposed due to the small amount of netlists found.

