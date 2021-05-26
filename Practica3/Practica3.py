#####################################
############ PRACTICA 6 #############
#####################################

import numpy as np


matSust=[[ 2,-7,-5,-7],
         [-7, 2,-7,-5],
         [-5,-7, 2,-7],
         [-7,-5,-7, 2]]

gapOpem=gapEXTEND= -5

def getMaximo():
    pass

def inciar(s1,s2,gapOpem): 

	M = np.zeros((len(s1)+1,len(s2)+1))

	token  = 0 

	for i in range(1,len(s2)+1):

		token = token + gapOpem
		M[0][i] = token
		
	token = 0 
	for i in range(1,len(s1)+1):

		token = token + gapOpem
		M[i][0] = token
		
	print(M)


#####################################

S1 = "AGC" #columna
S2 = "AAG" #Fila

inciar(S1,S2,gapOpem)