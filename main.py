import os

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
	dumper = 'fasterq-dump ' + acc + ' -O fastqs/fastq_dump'
	os.system(dumper)
'''

#Run fastqc	
fastq_files = os.listdir('fastqs/fastq_dump')	
fastqc_output = 'fastqs/fastqc_output/'

for file in fastq_files:
	fastqc = 'fastqc -o ' + fastqc_output + ' fastqs/fastq_dump/' + file
	os.system(fastqc)
