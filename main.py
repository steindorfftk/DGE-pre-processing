import os
import configuration
import time

start_time = time.time()

#Save accesion list
accession_list = []
with open('input/SraAccList.txt','r') as texto:
	for line in texto:
		linha = line.split()
		accession_list.append(linha[0])

#Download SRA data		
if configuration.verbose == True:
	print('Downloading SRA data...')
os.system('prefetch --option-file input/SraAccList.txt ')
if configuration.verbose == True:
	print('Done!\n')

#Convert SRA to fastq
for acc in accession_list:
	if configuration.verbose == True:
		print('Converting ' + acc + '.sra to fastq...')
	dumper = 'fasterq-dump ' + acc + ' -O temporary/fastq_dump'
	os.system(dumper)
	if configuration.verbose == True:
		print('Done!\n')	


#Run fastqc	
fastq_input = os.listdir('temporary/fastq_dump')	
fastqc_output = 'temporary/fastqc_output/'

for file in fastq_input:
	if '.fastq' in file:
		if configuration.verbose == True:
			print('Running fastqc for ' + file[:-4] + '...')	
		fastqc = 'fastqc -o ' + fastqc_output + ' temporary/fastq_dump/' + file	
		os.system(fastqc)
		if configuration.verbose == True:
			print('Done!\n')	
	

#bowtie2 setting
bowtie_input = os.listdir('temporary/fastq_dump/')
base_name = configuration.refGenomePath.replace('temporary/bowtie2/refGenomes/','').replace('.fasta','')
index = 'temporary/bowtie2/indexes/' + base_name + '/' + base_name

#Run bowtie2
for file in bowtie_input:
	if '.fastq' in file:
		if configuration.verbose == True:
			print('Running bowtie2 for ' + file[:-6] + '...')	
		genome = configuration.refGenomePath
		sequences = 'temporary/fastq_dump/' + file
		output = 'temporary/bowtie2/aligned/' + file[:-6] + '.sam'
		bowtie = 'bowtie2 -p 6 -x ' + index + ' -U ' + str(sequences) + ' -S ' + str(output)
		os.system(bowtie) 
		if configuration.verbose == True:
			print('Done!\n')

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")


		
#Run samtools - mapping stats	
samtools_input = os.listdir('temporary/bowtie2/aligned/')

for file in samtools_input:
	if '.sam' in file:
		if configuration.verbose == True:
			print('Converting ' + file + ' to .bam')
		input = 'temporary/bowtie2/aligned/' + file
		os.system('samtools view -bS ' + input + ' > temporary/samtools/bam_files/' + file[:-4] + '.bam') 		
		if configuration.verbose == True:
			print('Sorting ' + file[:-4] + '.bam')
		os.system('samtools sort temporary/samtools/bam_files/' + file[:-4] + '.bam -o temporary/samtools/bam_files_sorted/' + file[:-4] + '_sorted.bam') 	
		if configuration.verbose == True:
			print('Indexing ' + file[:-4] + '.bam')
		os.system('samtools index temporary/samtools/bam_files_sorted/' + file[:-4] + '_sorted.bam') 	
		if configuration.verbose == True:
			print('Mapping stats for ' + file[:-4] + '.bam')
		os.system('samtools flagstat temporary/samtools/bam_files_sorted/' + file[:-4] + '_sorted.bam > temporary/samtools/map_stats/' + file[:-4] + '_mapping_stats.txt')
		if configuration.verbose == True:
			print('Done!\n')


		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
