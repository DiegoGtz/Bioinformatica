#####################################
############ PRACTICA 6 #############
#####################################

import numpy as np

######################## Practica 6 ###########################
matSust=[[ 2,-7,-5,-7],
         [-7, 2,-7,-5],
         [-5,-7, 2,-7],
         [-7,-5,-7, 2]]

gapOpem=gapEXTEND= -5

vec1 = "ACGT"
vec2 = "ACGT"

def encontrar_valor(vec1, pos):
	for i in range(len(vec1)+1):
		if (vec1[i] == pos):
			return i

M1 = np.zeros((4,4))
M2 = []


mi_dicc = dict()
def getCamino(i,j,tipo):

	M2.append((i,j,tipo))

def getM():
	return M2
	
def clear():
	global M2
	M2 = []





def inciar(s1,s2,gapOpem): 

	pos_s1 = pos_s2 = ""
	
	M = np.zeros((len(s1)+1,len(s2)+1))

	token  = 0 

	for i in range(1,len(s2)+1):

		token = token + gapOpem
		M[0][i] = token

	token = 0 
	for i in range(1,len(s1)+1):

		token = token + gapOpem
		M[i][0] = token

	print "M = ", M

	print "S = ",matSust

	v = []

	for i in range(1, len(s2)+1):
		for j in range(1, len(s1)+1):

#			M[i][j]
			pos_s1 = s1[j-1]
			pos_s2 = s2[i-1]
		#	print(pos_s1, pos_s2)
			
			a = encontrar_valor(vec1, pos_s1)
			b = encontrar_valor(vec2, pos_s2)

		
			#print(v)
			
			f1 = M[i-1][j-1] + matSust[b][a]
			f2 = M[i-1][j] + gapOpem
			f3 = M[i][j-1] + gapOpem

			v.append(f1)
			v.append(f2)	
			v.append(f3)

			#print("Valors max", v)
			max1 = max(v)
			
			M[i][j] = max1

			if f1 == max1 : 
				getCamino(i-1,j-1,"d")
			if f2 == max1 : 
				getCamino(i-1,j,"T")
			if f3 == max1 : 
				getCamino(i,j-1,"L")

			
			mi_dicc[(i,j,)] = M2

			#print (a, b)
			#print (matSust[b][a])
			
			print(f1, " " ,f2, " ", f3)
			#print("maximo", max(v))	
			#print("***********************************************")

			f1=f2=f3=0
			v=[]
		
			clear()


		
	print("////////Resultado//////////")
	print  M	



S1 = "AAG" #Fila
S2 = "AGC" #columna



inciar(S1,S2,gapOpem) 
