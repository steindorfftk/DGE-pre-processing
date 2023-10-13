import os

#Configuration
refGenomePath = 'temporary/bowtie2/refGenomes/mm10.fasta'

#Save accesion list
accession_list = []
with open('input/SraAccList.txt','r') as texto:
	for line in texto:
		linha = line.split()
		accession_list.append(linha[0])
'''
#Download SRA data		
os.system('prefetch --option-file input/SraAccList.txt ')

#Convert SRA to fastq
for acc in accession_list:
	print('\nDumping ' + acc + '...')
	dumper = 'fasterq-dump ' + acc + ' -O temporary/fastq_dump'
	os.system(dumper)


#Run fastqc	
fastq_input = os.listdir('temporary/fastq_dump')	
fastqc_output = 'temporary/fastqc_output/'

for file i	'n fastq_input:
	fastqc = 'fastqc -o ' + fastqc_output + ' temporary/fastq_dump/' + file	
	os.system(fastqc)
'''	
#bowtie2 setting
bowtie_input = os.listdir('temporary/fastq_dump/')
base_name = refGenomePath.replace('temporary/bowtie2/refGenomes/','').replace('.fasta','')
index = 'temporary/bowtie2/indexes/' + base_name + '/' + base_name

#Run bowtie2
for file in bowtie_input:
	genome = refGenomePath
	sequences = 'temporary/fastq_dump/' + file
	output = 'temporary/bowtie2/' + file[:-6] + '.sam'
	bowtie = 'bowtie2 -x ' + index + ' -U ' + str(sequences) + ' -S ' + str(output)
	print(output)
	os.system(bowtie) 
	
	
	
	
	
	
	
	
	
	
	
