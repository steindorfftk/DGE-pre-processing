About me: This tool is intended to download gene expression data from SRA, convert it to fastq, run quality control, perform alignment and run differential expression analysis for a given list of SRA accession codes.

#Required installing (Linux):

#Installing SRA Tool kit
1 - Download link: https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit
2 - Unpack downloaded file
3.1 - Add binaries file to path (export PATH=$PATH:$PWD/sratoolkit.X.X.X-dist64/bin)
3.2 - Test if it worked: 'run which fastq-dump'. It should have a similar output as: '/Users/JoeUser/sratoolkit.3.0.0-mac64/bin/fastq-dump'
4.1 - Run 'vdb-config -i'. Use tab- and space/enter keys to navigate and select.
4.2 - Enable Remote Access in the main menu
4.3 - In the cache tab, enable local file-caching
4.4 - In the cache tab, add the path to '/easy_dea/sratoolkit_repository' to the "Location of user-repository"
5 - Test that toolkit is functional: run 'fastq-dump --stdout -X 2 SRR390728'. The output must be exaclty this: 
'Read 2 spots for SRR390728
Written 2 spots for SRR390728
@SRR390728.1 1 length=72
CATTCTTCACGTAGTTCTCGAGCCTTGGTTTTCAGCGATGGAGAATGACTTTGACAAGCTGAGAGAAGNTNC
+SRR390728.1 1 length=72
;;;;;;;;;;;;;;;;;;;;;;;;;;;9;;665142;;;;;;;;;;;;;;;;;;;;;;;;;;;;;96&&&&(
@SRR390728.2 2 length=72
AAGTAGGTCTCGTCTGTGTTTTCTACGAGCTTGTGTTCCAGCTGACCCACTCCCTGGGTGGGGGGACTGGGT
+SRR390728.2 2 length=72
;;;;;;;;;;;;;;;;;4;;;;3;393.1+4&&5&&;;;;;;;;;;;;;;;;;;;;;<9;<;;;;;464262'

#Installing fastqc
1 - Run sudo apt-get update
2 - Run sudo apt-get install fastqc
