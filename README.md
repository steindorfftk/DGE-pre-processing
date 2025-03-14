### DEG-pre-processing is a tool designed for the Bioinformatics Core of Clinician Hospital of Porto Alegre (HCPA). It automatically downloads gene expression data from the Sequence Read Archive (SRA), converts it to FASTQ format, conducts standard quality control procedures, performs alignment, and countins features for a specified list of SRA accession codes.
### Obs1: The instructions provided in the README are tailored for usage on Linux operating systems.
### Obs2: This version of the tool is currently optimized for processing unpaired reads exclusively.
### Obs3: Depending on your Linux distribution, there may be an issue with the sratoolkit package where it gets removed from the PATH file after a PC reboot. Consequently, you may need to re-add it to the PATH before using the program again, typically as part of step 5 in the "Required packages installation - SRA Tool Kit" section from this README.

# Input File Preparation
### Collecting SRA accession codes from Gene Expression Omnibus (The study must have a SRA Run Selector link)
- 1 - At the bottom of the geo accession display page, click on the SRA Run Selector link.
- 2 - In the SRA Run Selector webpage, click on 'Accession list' button from the 'Select' table.
- 3 - You can remove or add accession codes to the downloaded 'SRR_Acc_List.txt' file as needed, but the final file must keep the same name and structure (i.e. one accession code per line)
- 4 - Place the 'SRR_Acc_List.txt' file at the 'DEG-pre-processing-main/input' directory.

# Program configuration
- You have the option to define three variables within the 'DPP_configuration.py' file. 
- 1 - verbose: Set to False if you prefer the program not to print progress updates in the terminal during execution.
- 2 - lowmemory: Set to False if you prefer the program not to delete used files as it progresses through subsequent steps.
- 3 - organism: Set to 'Homo sapiens' or 'Mus musculus' according to your sample


# DEG-pre-processing utilization
- 1 - Make sure that the input 'SRR_Acc_List.txt' file is in the proper directory as indicated in the 'Input File Preparation' section and that the proper organism is selected as of 'Program configuration' section.
- 2 - Navigate to the 'DEG-pre-processing-main' directory.
- 3 - Run 'python3 main.py'

# You will three outputs for each Accession code:
- a) The .tabular file with gene counts
- b) The .html file with quality metrics from fastqc
- c) The .txt file with alignment metrics from bowtie2
