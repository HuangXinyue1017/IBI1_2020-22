import os
import re

# create a dictionary to store the code
dict = {'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
	    'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
	    'TAT':'Y','TAC':'Y','TAA':'O','TAG':'U',
	    'TGT':'C','TGC':'C','TGA':'X','TGG':'W',
	    'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
	    'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
	    'CAT':'H','CAC':'H','CAA':'Q','CAG':'Z',
	    'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
	    'ATT':'I','ATC':'I','ATA':'J','ATG':'M',
	    'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
	    'AAT':'N','AAC':'B','AAA':'K','AAG':'K',
	    'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
	    'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
	    'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
	    'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
	    'GGT':'G','GGC':'G','GGA':'G','GGG':'G'}

file = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")

# name name of sequences
# unknown_seq unknown sequences
name = []
unknown_seq = []
seq = ''
unknown = 0
for line in file.readlines():
	if (line[0] == '>'):
		if (unknown):
			unknown_seq.append(seq)
		if (re.search('unknown function',line)):
			unknown = 1
			en = line.find('_')
			name.append(line[1:en])
			seq = ''
		else:
			unknown = 0
	elif (unknown):
		line = line.strip()
		seq = seq + line
if (unknown):
	unknown_seq.append(seq)

file.close()

new_file = open("unknown_function.fa", "w")

# print answer
for i in range(0,len(name)):
	t = new_file.write(name[i] + ' ' + str(len(unknown_seq[i]))+'\n')
	t = new_file.write(unknown_seq[i] + '\n')

new_file.close()