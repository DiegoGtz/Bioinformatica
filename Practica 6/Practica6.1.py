#####################################
############ PRACTICA 6 #############
#####################################
import numpy as np

#from Bio import SeqIO

######################## Practica 6 ###########################
matSust=[[ 2,-7,-5,-7],
         [-7, 2,-7,-5],
         [-5,-7, 2,-7],
         [-7,-5,-7, 2]]

##Pregunta2
#//////////////////////////////////////////////////////
match = 2
missMatch = -2 

matSust1 = [[ match,missMatch,missMatch,missMatch],
         [missMatch, match,missMatch,missMatch],
         [missMatch,missMatch, match,missMatch],
         [missMatch,missMatch,missMatch, match ]]

#///////////////////////////////////////////////////////

gapOpem=gapEXTEND= -5

S1 = "AAG" #Fila
S2 = "AGC" #columna

vec1 = "ACGT"
vec2 = "ACGT"

ss1=""
ss2=""

'''def lectura():
    sequences = SeqIO.parse("P21333.fasta", "fasta")

    for record in sequences:
        data1 = str(record.seq.upper())

    sequences = SeqIO.parse("Q8BTM8.fasta", "fasta")
    for record in sequences:
        data2 = str(record.seq.upper())
    return data1,data2
'''
def encontrar_valor(vec1, pos):
	for i in range(len(vec1)+1):
		if (vec1[i] == pos):
			return i

def imprimir(M):
	for i in range(len(M)):
		for j in range(len(M)):
			print (M[i][j][3], end="\t")
		print()

def verificar (M,i,j):
	cont=0
	if(M[i][j][0] == 1):
		cont+=1
	if(M[i][j][1] == 1):
		cont+=1
	if(M[i][j][2] == 1):
		cont+=1
	return cont

def camino(M,i,j,ss1,ss2):
	global S1
	global S2

	if (verificar (M,i,j) == 1):
		if(M[i][j][0] == 1):
			#diagonal
			ss1 += S1[j-1]
			ss2 += S2[i-1]
			#print("diagonal",i-1," ",j-1)
			if(i==0 or j==0):
				print("Resultado: ")
				print(ss2)
				print(ss2)
				return
			camino(M,i-1,j-1,ss1,ss2)

		elif(M[i][j][1] == 1):
			#arriba
			ss1 += "-"
			ss2 += S2[i-1] 
			#print("arriba",i-1," ",j)
			if(i==0 or j==0):
				print("Resultado: ")
				print(ss1)
				print(ss2)
				return 
			camino(M,i-1,j,ss1,ss2)

		elif(M[i][j][2] == 1):
			#costado
			ss1 += S1[j-1] 
			ss2 += "-"
			#print("costado",i," ",j-1)
			if(i==0 or j==0):
				print("Resultado: ")
				print(ss1)
				print(ss2)
				return
			camino(M,i,j-1,ss1,ss2)

	elif(verificar(M,i,j) == 2):
		#print("ramificacion")
		if(M[i][j][0] == 1):
			#diagonal
			ss1 += S1[j-1]
			ss2 += S2[i-1]
			#print("diagonal",i-1," ",j-1)
			if(i==0 or j==0):
				print("Resultado: ")
				print(ss1)
				print(ss2)
				return
			camino(M,i-1,j-1,ss1,ss2)

		if(M[i][j][1] == 1):
			#arriba
			ss1 += "-"
			ss2 += S2[i-1] 
			#print("arriba",i-1," ",j)
			if(i==0 or j==0):
				print("Resultado: ")
				print(ss1)
				print(ss2)
				return 
			camino(M,i-1,j,ss1,ss2)

		if(M[i][j][2] == 1):
			#costado
			ss1 += S1[j-1] 
			ss2 += "-"
			#print("costado",i," ",j-1)
			if(i==0 or j==0):
				print("Resultado: ")
				print(ss1)
				print(ss2)
				return
			camino(M,i,j-1,ss1,ss2)

	elif(verificar(M,i,j) == 0):
		print("Resultado: ")
		print(ss1)
		print(ss2)
		
			
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
		#print ("token ", token)
		M_vacia[0][i][3] = token
		M_vacia[0][i][2] = 1

	token = 0
	for i in range(1,len(s1)+1):
		token = token + gapOpem
		M_vacia[i][0][3] = token
		M_vacia[i][0][1] = 1

	#print ("M = ", M_vacia)
	#print ("S = ",matSust)

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

			f1=f2=f3=0
			v=[]
		
	print("////////Resultado//////////")
	#print(M_vacia)
	imprimir(M_vacia)
	print("***********************************************")
	i=3
	j=3
	ss1 = ""
	ss2 = ""

	camino(M_vacia,i,j,ss1,ss2)

#data1,data2=lectura()
#print(len(data1))
#print(len(data2))

inciar(S1,S2,gapOpem) 
