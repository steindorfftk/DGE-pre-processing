### About DEG-pre-processing: This tool is intended to download gene expression data from SRA, convert it to fastq, run standard quality control, perform alignment and run differential expression analysis for a given list of SRA accession codes.
### Obs1: The instructions in the README are intended for use on Linux operating systems
### Obs2: This version is currently suited for unpaired reads only.


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
- 7 - Delete 'init.py' from 'DEG-pre-processing/temporary/sratoolkit/' 
- 8.1 - Run the command 'vdb-config -i'. Use tab- and space/enter keys to navigate and select. 
- 8.2 - Enable Remote Access in the main menu 
- 8.3 - In the cache tab, enable local file-caching 
- 8.4 - In the cache tab, add the path to '/DEG-pre-processing/temporary/sratoolkit' to the "Location of user-repository" 
- 8.5 - Save and exit 
- 9 - Test that toolkit is functional: run 'fastq-dump --stdout -X 2 SRR390728'. The output must be exaclty this: 'Read 2 spots for SRR390728 Written 2 spots for SRR390728 @SRR390728.1 1 length=72 CATTCTTCACGTAGTTCTCGAGCCTTGGTTTTCAGCGATGGAGAATGACTTTGACAAGCTGAGAGAAGNTNC +SRR390728.1 1 length=72 ;;;;;;;;;;;;;;;;;;;;;;;;;;;9;;665142;;;;;;;;;;;;;;;;;;;;;;;;;;;;;96&&&&( @SRR390728.2 2 length=72 AAGTAGGTCTCGTCTGTGTTTTCTACGAGCTTGTGTTCCAGCTGACCCACTCCCTGGGTGGGGGGACTGGGT +SRR390728.2 2 length=72 ;;;;;;;;;;;;;;;;;4;;;;3;393.1+4&&5&&;;;;;;;;;;;;;;;;;;;;;<9;<;;;;;464262'

#### bowtie2
- 1 - Run 'sudo apt install bowtie2'
- 2 - Download the reference genomes of Homo sapiens and Mus musculus from the right menu on https://bowtie-bio.sourceforge.net/bowtie2/manual.shtml (Homo sapiens index: H. sapiens, GRCh38 no-alt analysis set; Mus musculus index: M. Musculus, mm10)
- 3 - Place the indexes into DEG-preprocessing/temporary/bowtie2/indexes/ directory.

#### featureCounts
- 1.1 - Make a directory to install mini conda in the installation directory of your choice (mkdir -p miniconda3)
- 1.2 - Change into miniconda3 directory
- 1.3 - Download miniconda (wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh)
- 1.4 - Run miniconda installation script (bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3)
- 1.5 - Remove miniconda installation script (rm -rf ~/miniconda3/miniconda.sh)
- 1.6 - Initiallize miniconda3 ($PWD/bin/conda init bash)
- 2.1 - Download features counts (conda install -c bioconda subread)
- 2.2 - Test that featureCounts was installed (which featureCounts). It should have a similar output as: '/home/User/miniforge3/bin/featureCounts'
- The gene annotations at 'DEG-pre-processing/feature_counts/data' are updated as of february 2024. They were downloaded from Rsubread repository: https://code.bioconductor.org/browse/Rsubread/tree/RELEASE_3_9/inst/annot/

#### fastqc
- 1 - Run 'sudo apt-get install fastqc'

#### samtools
- 1 - Run 'sudo apt-get install samtools'

# Input File Preparation
- This program is suitable to scrape data from any list of studies found after a Gene Expression Omnibus (GEO) search. The input file must be one or more html files with search results. Prepare the file as following:
- 1 - Perform the GEO search with the proper key words or GEO accessions (https://www.ncbi.nlm.nih.gov/geo/) + apply desired filters.
- 2 - If the search returns more than 20 results, click on '20 per page' and change the items per page as necessary.
- 3 - Right click on the page, select 'Save Page As' and save the page as .html.
- 4 - If the search returns more than 500 results you can save more than one page with another name and use it along the first one.


# GEO_scraper Utilization
- 1 - Add the GEO search results html files in the input directory (GEO_scraper-main/input)
- 2 - In-script configuration: there are 3 variables you can define in-script - verbose, tissue and output_name.
- 2.1 - verbose: set to 'True' if you want the terminal to print the information while you are scraping, either else keep on 'False'. This doesn't alter the execution time or the final output.
- 2.2 - complete: set to 'True' if you want the program to gather information on Tissue type and Cell type from the studies. This considerably increases the execution time but it's recommended.
- 2.3 - output_name: set the desired output file name. The standard name is 'output'.
- 3 - Run the main.py file (python3 main.py)
- 4 - A .csv file with basic information about these studies will be created in output folder

