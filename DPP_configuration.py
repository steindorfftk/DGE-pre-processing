#Configuration
verbose = True
lowmemory = True
organism = 'Homo sapiens' #Homo sapiens or Mus musculus


#Paths
if organism == 'Mus musculus':
	refGenomePath = 'temporary/bowtie2/refGenomes/mm10.fasta'
	annotationPath = 'temporary/feature_counts/data/mm10_RefSeq_exon.txt'
elif organism == 'Homo sapiens':
	refGenomePath = 'temporary/bowtie2/refGenomes/GRCh38_noalt_as'
	annotationPath = 'temporary/feature_counts/data/hg38_RefSeq_exon.txt'
