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

S1 = "AAG" #Fila
S2 = "AGC" #columna

vec1 = "ACGT"
vec2 = "ACGT"

news1 = ""
news2 = ""

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

def imprimir(M):
	for i in range(len(M)):
		for j in range(len(M)):
			print (M[i][j][3], end="\t")
		print()

def camino(M):
	global news1
	global news2
	global S1
	global S2
	
	for i in range(len(M)-1,-1,-1):
		for j in range(len(M)-1,-1,-1):
			#print(M[i][j][3], end="\t")
			if(M[i][j][0] == 1):
				#diagonal
				news1 += S1[j-1]
				news2 += S2[i-1]
			
			if(M[i][j][1] == 1):
				#arriba
				news1 += "-"
				news2 += S2[i-1] 
				print(news1)
				print(news2)
				return
			if(M[i][j][2] == 1):
				#costado
				news1 += S1[j-1] 
				news2 += "-"
			print(news1)
			print(news2)
			break
		
		print()
		
		
			
def inciar(s1,s2,gapOpem): 

	pos_s1 = pos_s2 = ""
	
	M = np.zeros((len(s1)+1,len(s2)+1))
	A = [0,0,0,0]
	M_vacia = []
	vector_vacio = []
	
	
	for i in range(len(s2)+1):
		for j in range(len(s1)+1):
			vector_vacio.append(A.copy())
		M_vacia.append(vector_vacio)
		vector_vacio = []
	
	token  = 0
	for i in range(1,len(s2)+1):
		token = token + gapOpem
		print ("token ", token)
		M_vacia[0][i][3] = token

	token = 0
	for i in range(1,len(s1)+1):
		token = token + gapOpem
		M_vacia[i][0][3] = token

	print ("M = ", M_vacia)

	print ("S = ",matSust)

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
			
			f1 = M_vacia[i-1][j-1][3] + matSust[b][a]
			f2 = M_vacia[i-1][j][3] + gapOpem
			f3 = M_vacia[i][j-1][3] + gapOpem

			v.append(f1)
			v.append(f2)	
			v.append(f3)

			#print("Valors max", v)
			max1 = max(v)
			
			M_vacia[i][j][3] = max1
			
			
			if f1 == max1 : 
				M_vacia[i][j][0] = 1
			if f2 == max1 : 
				M_vacia[i][j][1] = 1
			if f3 == max1 : 
				M_vacia[i][j][2] = 1

			#mi_dicc[(i,j,)] = M2

			#print (a, b)
			#print (matSust[b][a])
			
			#print(f1, " " ,f2, " ", f3)
			#print("maximo", max(v))	
			#print("***********************************************")

			f1=f2=f3=0

			v=[]
#		imprimir(M_vacia)
#		return
		
	print("////////Resultado//////////")
	print(M_vacia)
	imprimir(M_vacia)
	print("***********************************************")
	camino(M_vacia)
	
#	print(len(M))




inciar(S1,S2,gapOpem) 

