import os
import configuration
import paths
import time

start_time = time.time()

#Save accesion list
accession_list = []
with open('input/SRR_Acc_List.txt','r') as texto:
	for line in texto:
		linha = line.split()
		accession_list.append(linha[0])

done_check = []

#Download SRA data		
if configuration.verbose == True:
	print('Downloading SRA data...')
os.system('prefetch --option-file input/SRR_Acc_List.txt ')
if configuration.verbose == True:
	isdone = True
	prefetch_done = os.listdir('temporary/sratoolkit/sra')
	for file in prefetch_done:
		done_check.append(file[:-4])
	for acc in accession_list:
		if acc not in done_check:
			isdone = False
	if isdone == True:
		print('Done!\n')
	else:
		print('Error downloading one or more SRA files')

done_check = []

#Convert SRA to fastq
for acc in accession_list:
	if configuration.verbose == True:
		print('Converting ' + acc + '.sra to fastq (fasterq-dump) ...')
	dumper = 'fasterq-dump ' + acc + ' -O temporary/fastq_dump'
	os.system(dumper)
	if configuration.verbose == True:
		fastqdump_done = os.listdir('temporary/fastq_dump')
		for file in fastqdump_done:
			done_check.append(file[:-6])
		if acc in done_check:
			print('Done!\n')
		else:
			print(f'Error converting {acc}.sra to .fastq')			

#Delete SRA files
if configuration.lowmemory == True:
	sra_files = os.listdir('temporary/sratoolkit/sra')
	for file in sra_files:
		path = 'temporary/sratoolkit/sra/' + file
		os.remove(path)


#Run fastqc	
fastq_input = os.listdir('temporary/fastq_dump')	
fastqc_output = 'temporary/fastqc_output/'

for file in fastq_input:
	if '.fastq' in file:
		if configuration.verbose == True:
			print('Running quality control for ' + file + ' (fastqc) ...')	
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
			print('Aligning ' + file[:-6] + ' reads with reference genome (bowtie2)...')	
		genome = configuration.refGenomePath
		sequences = 'temporary/fastq_dump/' + file
		output = 'temporary/bowtie2/aligned/' + file[:-6] + '.sam'
		bowtie = 'bowtie2 -p 6 -x ' + index + ' -U ' + str(sequences) + ' -S ' + str(output)
		os.system(bowtie) 
		if configuration.verbose == True:
			print('Done!\n')


#Delete fastq files
if configuration.lowmemory == True:
	sra_files = os.listdir('temporary/fastq_dump')
	for file in sra_files:
		path = 'temporary/fastq_dump/' + file
		os.remove(path)

		
#Run samtools - mapping stats	
samtools_input = os.listdir('temporary/bowtie2/aligned/')

for file in samtools_input:
	if '.sam' in file:
		if configuration.verbose == True:
			print('Sorting ' + file[:-4] + '.bam')
		os.system('samtools sort temporary/bowtie2/aligned/' + file + ' -O bam -o temporary/samtools/bam_files_sorted/' + file[:-4] + '_sorted.bam') 	
#		if configuration.verbose == True:
#			print('Indexing ' + file[:-4] + '.bam')
#		os.system('samtools index temporary/samtools/bam_files_sorted/' + file[:-4] + '_sorted.bam') 	
#		if configuration.verbose == True:
#			print('Mapping stats for ' + file[:-4] + '.bam')
#		os.system('samtools flagstat temporary/samtools/bam_files_sorted/' + file[:-4] + '_sorted.bam > temporary/samtools/map_stats/' + file[:-4] + '_mapping_stats.txt')
		if configuration.verbose == True:
			print('Done!\n')


#Delete aligned files
if configuration.lowmemory == True:
	sra_files = os.listdir('temporary/bowtie2/aligned')
	for file in sra_files:
		path = 'temporary/bowtie2/aligned/' + file
		os.remove(path)


#Run feature counts	
featurecounts_input = os.listdir('temporary/samtools/bam_files_sorted/')

for file in featurecounts_input:
	if '.bam' in file and '.bam.' not in file:
		if configuration.verbose == True:
			print('Counting features for ' + file + ' (featureCounts)')
		os.system('featureCounts -a ' + configuration.annotationPath + ' -F "SAF" -o temporary/feature_counts/output/' + file[:-4] + '.txt temporary/samtools/bam_files_sorted/' + file)

		if configuration.verbose == True:
			print('Done!\n')


#Delete bam sorted files
if configuration.lowmemory == True:
	sra_files = os.listdir('temporary/samtools/bam_files_sorted/')
	for file in sra_files:
		path = 'temporary/samtools/bam_files_sorted/' + file
		os.remove(path)


#Extract feature counts data to a tabular file
output_input = os.listdir('temporary/feature_counts/output/')






for file in output_input:
	if '.txt' in file and '.txt.' not in file:
		inputName = 'temporary/feature_counts/output/' + file
		outputName = 'output/' + file[:-4] + '.tabular'
		os.system("sed -i '/^#/d' " + inputName)
		os.system('cut -f 1,7 ' + inputName + ' > ' + outputName) 



#Delete feature counts output files
if configuration.lowmemory == True:
	sra_files = os.listdir('temporary/feature_counts/output/')
	for file in sra_files:
		path = 'temporary/feature_counts/output/' + file
		os.remove(path)
							
#Print elapsed time	
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
