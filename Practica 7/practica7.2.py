import sys
import numpy as np
from Bio import SeqIO

def local_alignment(d, seq1, seq2):

	for i in range(1,row):
		for j in range(1, column):
			value = identicalMatch
			
			if seq2[i-1] != seq1[j-1]:
				value = mismatch  
			Diag = F[i-1][j-1] + value
			Top = F[i-1][j] + gapOpem
			Left = F[i][j-1] + gapOpem
			F[i][j] = max(Diag,Top,Left,0)

	print() 
	print ("*"*50)
	print("Matriz :")
	print (F)		

	mayor = -5000
	i = 0
	j = 0
	for r in range(1,row):
		for c in range(1, column):
			if F[r][c]>mayor:
				i = r
				j = c
				mayor = F[r][c]

	alignmented_seq1 = ""
	alignmented_seq2 = ""

	
	while (i > 0 or j > 0):

		value = identicalMatch
		if seq2[i-1] != seq1[j-1]:
			value = mismatch  

		if (i>0 and j>0 and F[i][j] == F[i-1][j-1] + value):		
			alignmented_seq1 = seq1[j-1] + alignmented_seq1
			alignmented_seq2 = seq2[i-1] + alignmented_seq2
			i = i-1
			j = j-1

		elif (i>0 and F[i][j]==F[i-1][j]+gapOpem):
			alignmented_seq1 = "-" + alignmented_seq2	
			alignmented_seq2 = seq2[i-1] + alignmented_seq2
			i = i-1

		else:
			alignmented_seq2 = "-" + alignmented_seq2
			alignmented_seq1 = seq1[j-1] + alignmented_seq1
			j = j-1	

		if F[i][j]==0:
			break	


	print ()		
	print (alignmented_seq1)
	print ()
	print (alignmented_seq2)			
	

def lectura():
    sequences = SeqIO.parse("P21333.fasta", "fasta")

    for record in sequences:
        data1 = str(record.seq.upper())

    sequences = SeqIO.parse("Q8BTM8.fasta", "fasta")
    for record in sequences:
        data2 = str(record.seq.upper())
    return data1,data2

if __name__ == "__main__":

	gapOpem = -5
	identicalMatch = 2
	mismatch = -2
	seq1,seq2 = lectura()

	print("*"*50)
	print("Entradas : ")
	print(seq1)
	print()
	print(seq2)
	print("*"*50)

	column = len(seq1)+1
	row = len(seq2)+1

	F = np.zeros([row, column], dtype=int) 

	local_alignment(gapOpem, seq1, seq2)	