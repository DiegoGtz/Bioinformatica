from random import randint, uniform,random
from Bio import SeqIO

query = "GSVEDTTGSQSLAALLNKCKTPQGKRLUVNQWIKQPLMDKNRIEERLNLVEAFVEDAELRQTLQEDL"

principal = "ARNDCQEGHILKMFPSTWYVBJZX"

blom62 = [[4,-1,-2,-2,0,-1,-1,0,-2,-1,-1,-1,-1,-2,-1,1,0,-3,-2,0,-2,-1,-1,-1,-4],
		  [-1,5,0,-2,-3,1,0,-2,0,-3,-2,2,-1,-3,-2,-1,-1,-3,-2,-3,-1,-2,0,-1,-4],
		  [-2,0,6,1,-3,0,0,0,1,-3,-3,0,-2,-3,-2,1,0,-4,-2,-3,4,-3,0,-1,-4],
		  [-2,-2,1,6,-3,0,2,-1,-1,-3,-4,-1,-3,-3,-1,0,-1,-4,-3,-3,4,-3,1,-1,-4],
		  [0,-3,-3,-3,9,-3,-4,-3,-3,-1,-1,-3,-1,-2,-3,-1,-1,-2,-2,-1,-3,-1,-3,-1,-4],
		  [-1,1,0,0,-3,5,2,-2,0,-3,-2,1,0,-3,-1,0,-1,-2,-1,-2,0,-2,4,-1,-4],
		  [-1,0,0,2,-4,2,5,-2,0,-3,-3,1,-2,-3,-1,0,-1,-3,-2,-2,1,-3,4,-1,-4],
		  [0,-2,0,-1,-3,-2,-2,6,-2,-4,-4,-2,-3,-3,-2,0,-2,-2,-3,-3,-1,-4,-2,-1,-4],
		  [-2,0,1,-1,-3,0,0,-2,8,-3,-3,-1,-2,-1,-2,-1,-2,-2,2,-3,0,-3,0,-1,-4],
		  [-1,-3,-3,-3,-1,-3,-3,-4,-3,4,2,-3,1,0,-3,-2,-1,-3,-1,3,-3,3,-3,-1,-4],
		  [-1,-2,-3,-4,-1,-2,-3,-4,-3,2,4,-2,2,0,-3,-2,-1,-2,-1,1,-4,3,-3,-1,-4],
		  [-1,2,0,-1,-3,1,1,-2,-1,-3,-2,5,-1,-3,-1,0,-1,-3,-2,-2,0,-3,1,-1,-4],
		  [-1,-1,-2,-3,-1,0,-2,-3,-2,1,2,-1,5,0,-2,-1,-1,-1,-1,1,-3,2,-1,-1,-4],
		  [-2,-3,-3,-3,-2,-3,-3,-3,-1,0,0,-3,0,6,-4,-2,-2,1,3,-1,-3,0,-3,-1,-4],
		  [-1,-2,-2,-1,-3,-1,-1,-2,-2,-3,-3,-1,-2,-4,7,-1,-1,-4,-3,-2,-2,-3,-1,-1,-4],
		  [1,-1,1,0,-1,0,0,0,-1,-2,-2,0,-1,-2,-1,4,1,-3,-2,-2,0,-2,0,-1,-4],
		  [0,-1,0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1,1,5,-2,-2,0,-1,-1,-1,-1,-4],
		  [-3,-3,-4,-4,-2,-2,-3,-2,-2,-3,-2,-3,-1,1,-4,-3,-2,11,2,-3,-4,-2,-2,-1,-4],
		  [-2,-2,-2,-3,-2,-1,-2,-3,2,-1,-1,-2,-1,3,-3,-2,-2,2,7,-1,-3,-1,-2,-1,-4],
		  [0,-3,-3,-3,-1,-2,-2,-3,-3,3,1,-2,1,-1,-2,-2,0,-3,-1,4,-3,2,-2,-1,-4],
		  [-2,-1,4,4,-3,0,1,-1,0,-3,-4,0,-3,-3,-2,0,-1,-4,-3,-3,4,-3,0,-1,-4],
		  [-1,-2,-3,-3,-1,-2,-3,-4,-3,3,3,-3,2,0,-3,-2,-1,-2,-1,2,-3,3,-3,-1,-4],
		  [-1,0,0,1,-3,4,4,-2,0,-3,-3,1,-1,-3,-1,0,-1,-2,-2,-2,0,-3,4,-1,-4],
		  [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-4],
		  [-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,1]]

def lectura():
    sequences = SeqIO.parse("Q8BTM8.fasta", "fasta")
    for record in sequences:
        data = str(record.seq.upper())
    return data

#query = lectura()

#################################################################
def aleatorio():

	return randint(0,2)

def score(temp, var):
	contador = 0
	global principal
	#print(temp)
	#print(var)
	
	temp = list(temp)
	var = list(var)
	
	for i in range(3):
		a = principal.index(temp[i])
		b = principal.index(var[i])		
		
		#print(blom62[a][b])
		contador += blom62[a][b]
	return contador

def palabra():
	var = ""

	for i in range(len(query)-2):
		var = query[i] + query[i+1] + query[i+2]
		#print (var)
		
		random = aleatorio()
		#print ("ale:", random)
		
		temp = var
		vect_score = []
		
		for j in range(len(principal)):
			var = list(var)
			var[random] = principal[j]
			var = ''.join(var)
			#print (var)
			
			verif = score(temp, var)
			#print(verif)
			
			if (verif >= 13):
				vect_score.append(var)
				#print("mayor: ",verif) 
#			return
		return vect_score
		return 

#################################################################
def lectura2(file):
    sequences = SeqIO.parse(file, "fasta")
    for record in sequences:
        data = str(record.seq.upper())
    return data

def lectura3(file,a):
	#tell() obtener posicion
	#seek() ir a la posicion
	vector = a
	vecto_final= []
	for i in range (len(vector)):
		f=open(file, "r") 
		var1 = vector[i]
		var2 = []
		cont = 0
		linea=f.readline()
		#print(len(linea))
		posi=f.tell()
		linea=f.readline()
		#print(len(linea))
		while linea != "":
			#linea=linea[:-1]
			#print(posi,"  ",linea[:-1])
			temp= posi
			for i in range(len(linea)-2):
				a = linea[i]
				b = linea[i+1]
				c = linea[i+2]

				if c == '\n':
					posi=f.tell()
					#print(posi)
					linea=f.readline()

					if linea == "":
						break
					c = linea[0]
					caract = a+b+c
					if caract == var1:
						cont = cont + 1
						var2.append(temp+i)
						#print("------------------")
					#print(caract)

					a =  b
					b  = c
					c =  linea[1]
					caract = a+b+c
					if caract == var1:
						cont = cont + 1
						var2.append(temp+1+i)
						#print("------------------")
					#print(caract)
				else:
					caract = a+b+c
					if caract == var1:
						cont = cont + 1
						var2.append(temp+i)
						#print("------------------")
					#print(caract)	
			temp=posi
		#print("contador:", cont)
		#print (vector)
		#print(var1, var2)
		p=[]
		p.append(var1)
		p.append(var2)
		vecto_final.append(p)
	print(vecto_final)

def compara(lec,a):
	var=0 
	cad= ""
	# GSI 
	# MNMSRQ0GIFQ
	#  NMSRQGIFQ
	for j in range (len(a)):
		cad= a[j]
		#print (cad)
		for i in range (len(lec)-2):
			if (cad[0]== lec[i] and cad[1]== lec[i+1] and cad[2]== lec[i+2]):
				var+=1

		print (var, cad)
		var=0

def archivos():
	a=palabra()
	for i in range(1,12):
		file = "Dataset/" + str(i) + ".fasta"
		print(file)
		lectura3(file,a)
		#compara(lec,a)


archivos()


