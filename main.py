import os

#Save accesion list
accession_list = []
with open('input/SraAccList.txt','r') as texto:
	for line in texto:
		linha = line.split()
		accession_list.append(linha[0])
		
os.system('prefetch --option-file input/SraAccList.txt ')

for acc in accession_list:
	print('\nDumping ' + acc + '...')
	dumper = 'fasterq-dump ' + acc + ' -O fastqs/fastq_dump'
	os.system(dumper)
