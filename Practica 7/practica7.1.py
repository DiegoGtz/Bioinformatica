import sys
import numpy as np


def get_sequences(F, i, j, alignmented_seq1 = "", alignmented_seq2 = ""):
	if F[i][j][0]==0:
		print("\t\t Alineamiento ")		
		print (alignmented_seq1)
		print (alignmented_seq2)	
		return
	if i > 0 or j > 0:			
		if (i>0 and j>0 and F[i][j][1] == 'D'):		
			alignmented_seq1 = seq1[j-1] + alignmented_seq1
			alignmented_seq2 = seq2[i-1] + alignmented_seq2
			i = i-1
			j = j-1
		elif (i>0 and F[i][j][1]=='U'):
			alignmented_seq1 = "-" + alignmented_seq2	
			alignmented_seq2 = seq2[i-1] + alignmented_seq2
			i = i-1
		else:
			alignmented_seq2 = "-" + alignmented_seq2
			alignmented_seq1 = seq1[j-1] + alignmented_seq1
			j = j-1
		get_sequences(F, i, j, alignmented_seq1, alignmented_seq2)			

def local_alignment(F, i=1, j=1):



	diag = F[i-1][j-1][0] + matrix_sus[vec1[seq2[i-1]]][vec1[seq1[j-1]]]
	up = F[i-1][j][0] + d
	left = F[i][j-1][0] + d
	F[i][j][0]	= max(diag, up, left, 0)
	if F[i][j][0]==diag:
		F[i][j][1] = 'D'	
	if F[i][j][0]==up:	
		F[i][j][1] = 'U'
	if F[i][j][0]==left:	
		F[i][j][1] = 'L'
	#print(i,j)
	#print(F)
	if i==row-1 and j==column-1:
		
		print(F)
		mayor = -5000
		s_i = 0
		s_j = 0 
		for r in range(1,row):
			for c in range(1, column):
				if F[r][c][0]>=mayor:
					s_i = i
					s_j = j
					i = r
					j = c
					mayor = F[r][c][0]
		get_sequences(F, i, j)
		get_sequences(F, s_i, s_j)
		return
	if j<column-1:
		local_alignment(F, i ,j+1)	
	else:	
		local_alignment(F, i+1 ,1)
if __name__ == "__main__":
	d = -5 
	vec1 = {'A':0,'C':1,'G':2,'T':3}
	matrix_sus =  [[ 2,-7,-5,-7],
        		   [-7, 2,-7,-5],
        		   [-5,-7, 2,-7],
        		   [-7,-5,-7, 2]]

	match = 2


	print (matrix_sus)
	print()
	seq1 = "AAG"
	seq2 = "AGC"

	print("*"*50)
	print("\t 	Secuencias  ")
	print("Secuencia 1 : ", seq1)
	print("Secuencia 1 : ", seq2)
	print("*"*50)
	column = len(seq1)+1
	row = len(seq2)+1
	#print("Tamanio matriz : ", column, row)
	F = np.zeros([row, column], dtype='i,O') 
	print("*"*50)
	print("\t\t Matriz" )
	print()
	print(F)
	print("*"*50)
	print("\t\t Camino ")
	print()
	print("*"*50)

	local_alignment(F)

