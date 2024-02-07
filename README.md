### DEG-pre-processing is a tool designed for downloading gene expression data from the Sequence Read Archive (SRA), converting it to FASTQ format, conducting standard quality control procedures, performing alignment, and executing differential expression analysis for a specified list of SRA accession codes.
### Obs1: The instructions provided in the README are tailored for usage on Linux operating systems.
### Obs2: This version of the tool is currently optimized for processing unpaired reads exclusively.
### Obs3: Depending on your Linux distribution, there may be an issue with the sratoolkit package where it gets removed from the PATH file after a PC reboot. Consequently, you may need to re-add it to the PATH before using the program again, typically as part of step 5 in the "Required packages installation - SRA Tool Kit" section from this README.


# Program Installation
- 1 - Download the program files: Click on '<> Code' and then on 'Download ZIP'
- 2 - Place the 'DEG-pre-processing-main.zip' file on the installation directory of your choice.
- 3 - Change into the installation directory and unzip the program files (unzip DEG-pre-processing-main.zip)  

# Required packages Installation
#### SRA Tool kit 
- 1 - Download SRA tool kit from https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit. For Linux, click on 'Ubuntu Linux 64 bit architecture' to download the file.
- 2 - Place the 'sratoolkit.X.X.X-ubuntu64.tar.gz' file on the installation directory of your choice. (Replace X.X.X for the appropriate downloaded version)
- 3 - Change into the installation directory and uzip the program files (tar -xzf sratoolkit.X.X.X-ubuntu64.tar.gz)
- 4 - Change into sratoolkit.X.X.X-ubuntu64 directory.
- 5 - Add SRA Tool kit binaries file to path (export PATH=$PATH:$PWD/bin).  
- 6 - Test that it was added to path: run 'which fastq-dump'. It should have a similar output as: '/Users/JoeUser/sratoolkit.3.0.0-mac64/bin/fastq-dump'
- 7 - Delete 'init.py' from 'DEG-pre-processing-main/temporary/sratoolkit/' 
- 8.1 - Run the command 'vdb-config -i'. Use tab- and space/enter keys to navigate and select. 
- 8.2 - Enable Remote Access in the main menu 
- 8.3 - In the cache tab, enable local file-caching 
- 8.4 - In the cache tab, add the path to '/DEG-pre-processing-main/temporary/sratoolkit' to the "Location of user-repository" 
- 8.5 - Save and exit 
- 9.1 - Test that toolkit is functional: run 'fastq-dump --stdout -X 2 SRR390728'.
- 9.2 - The output must be exaclty this: 'Read 2 spots for SRR390728 Written 2 spots for SRR390728 @SRR390728.1 1 length=72 CATTCTTCACGTAGTTCTCGAGCCTTGGTTTTCAGCGATGGAGAATGACTTTGACAAGCTGAGAGAAGNTNC +SRR390728.1 1 length=72 ;;;;;;;;;;;;;;;;;;;;;;;;;;;9;;665142;;;;;;;;;;;;;;;;;;;;;;;;;;;;;96&&&&( @SRR390728.2 2 length=72 AAGTAGGTCTCGTCTGTGTTTTCTACGAGCTTGTGTTCCAGCTGACCCACTCCCTGGGTGGGGGGACTGGGT +SRR390728.2 2 length=72 ;;;;;;;;;;;;;;;;;4;;;;3;393.1+4&&5&&;;;;;;;;;;;;;;;;;;;;;<9;<;;;;;464262'

#### bowtie2
- 1 - Run 'sudo apt install bowtie2'
- 2 - Download the reference genomes of Homo sapiens and Mus musculus from the right menu on https://bowtie-bio.sourceforge.net/bowtie2/manual.shtml (Homo sapiens index: H. sapiens, GRCh38 no-alt analysis set; Mus musculus index: M. Musculus, mm10)
- 3 - Place the indexes into DEG-pre-processing-main/temporary/bowtie2/indexes/ directory.

#### featureCounts
- 1.1 - Make a directory to install miniconda in the installation directory of your choice (mkdir -p miniconda3)
- 1.2 - Change into miniconda3 directory
- 1.3 - Download miniconda by executing (wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh)
- 1.4 - Run miniconda installation script (bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3)
- 1.5 - Remove miniconda installation script (rm -rf ~/miniconda3/miniconda.sh)
- 1.6 - Initiallize miniconda3 ($PWD/bin/conda init bash)
- 2.1 - Download features counts (conda install -c bioconda subread)
- 2.2 - Test that featureCounts was installed (which featureCounts). It should have a similar output as: '/home/User/miniforge3/bin/featureCounts'
- The gene annotations at 'DEG-pre-processing-main/feature_counts/data' are updated as of february 2024. They were downloaded from Rsubread repository: https://code.bioconductor.org/browse/Rsubread/tree/RELEASE_3_9/inst/annot/(mkdir -p miniconda3)
- 1.2 - Change into miniconda3 directory
- 1.3 - Download miniconda (wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh)
- 1.4 - Run miniconda installation script (bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3)
- 1.5 - Remove miniconda installation script (rm -rf ~/miniconda3/miniconda.sh)
- 1.6 - Initiallize miniconda3 ($PWD/bin/conda init bash)
- 2.1 - Download features counts (conda install -c bioconda subread)
- 2.2 - Test that featureCounts was installed correctly by checking its location using the command: (which featureCounts). It should have a similar output as: '/home/User/miniforge3/bin/featureCounts'
- The gene annotations located at 'DEG-pre-processing-main/feature_counts/data' have been updated as of February 2024. They were retrieved from the Rsubread repository: https://code.bioconductor.org/browse/Rsubread/tree/RELEASE_3_9/inst/annot/

#### fastqc
- 1 - Run 'sudo apt-get install fastqc'

#### samtools
- 1 - Run 'sudo apt-get install samtools'

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
