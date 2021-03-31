import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

file_name = input()
file = open(file_name, "r")

# name name of sequences
# pro amino acids of sequences
name = []
pro = []
seq = ''
for line in file.readlines():
	if (line[0] == '>'):
		if (seq != ''):
			# from DNA to protein
			f = 0
			a = ''
			for t in range(0,(int)(len(seq)/3)):
				a = a + dict[seq[f:f+3]]
				f = f + 3
			pro.append(a)
		en = line.find('_')
		name.append(line[1:en])
		seq = ''
	else:
		line = line.strip()
		seq = seq + line

file.close()

new_file = open("unknown_function.fa", "w")

# print answer
for i in range(0,len(name)-1):
	t = new_file.write(name[i] + ' ' + str(len(pro[i]))+'\n')
	t = new_file.write(pro[i] + '\n')

new_file.close()