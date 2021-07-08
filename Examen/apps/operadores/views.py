from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.views.generic import CreateView
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import Storage
from django.core.files.base import ContentFile

#####################################################

#import cv2 
import numpy as np
from matplotlib import pyplot as plt 
import	re, math 

def inicio(request):
    return render(request,'Home.html')



class Algoritmos2():

	def __init__(self,s1,s2,gap,m1,m2):
		self.gapOpem = gap
		self.S1 = s1 #Fila
		self.S2 = s2 #columna
		self.identicalMatch = m1
		self.mismatch = m2
		self.ss1=""
		self.ss2=""

		self.column = len(self.S1)+1
		self.row = len(self.S2)+1

		self.vec = []

		self.Solution = []


   
		self.vec1 = {'A':0,'C':1,'G':2,'T':3}
		self.matrix_sus =  [[ 2,-7,-5,-7],
	        		   [-7, 2,-7,-5],
	        		   [-5,-7, 2,-7],
	        		   [-7,-5,-7, 2]]

	###########Pegarlo Aqui Javox#############

	def encontrar_valor(self,vec1,pos):

		for i in range(len(vec1)+1):
			if (vec1[i] == pos):
				return i

	def verificar (self,M,i,j):
		cont=0
		if(M[i][j][0] == 1):
			cont+=1
		if(M[i][j][1] == 1):
			cont+=1
		if(M[i][j][2] == 1):
			cont+=1
		return cont
	
	def camino(self,M,i,j,ss1,ss2):
		S1 = self.S1
		S2 = self.S2
		if (self.verificar (M,i,j) == 1):
			if(M[i][j][0] == 1):
				#diagonal
				ss1 += S1[j-1]
				ss2 += S2[i-1]
				#print("diagonal",i-1," ",j-1)
				if(i==0 or j==0):
					print("Resultado: ")
					self.vec.append(ss1)
					self.vec.append(ss2)
					print(ss2)
					print(ss2)
					return
				self.camino(M,i-1,j-1,ss1,ss2)

			elif(M[i][j][1] == 1):
				#arriba
				ss1 += "-"
				ss2 += S2[i-1] 
				#print("arriba",i-1," ",j)
				if(i==0 or j==0):
					print("Resultado: ")
					self.vec.append(ss1)
					self.vec.append(ss2)
					print(ss1)
					print(ss2)
					return 
				self.camino(M,i-1,j,ss1,ss2)

			elif(M[i][j][2] == 1):
				#costado
				ss1 += S1[j-1] 
				ss2 += "-"
				#print("costado",i," ",j-1)
				if(i==0 or j==0):
					print("Resultado: ")
					self.vec.append(ss1)
					self.vec.append(ss2)
					print(ss1)
					print(ss2)
					return
				self.camino(M,i,j-1,ss1,ss2)

		elif(self.verificar(M,i,j) == 2):
			#print("ramificacion")
			if(M[i][j][0] == 1):
				#diagonal
				ss1 += S1[j-1]
				ss2 += S2[i-1]
				#print("diagonal",i-1," ",j-1)
				if(i==0 or j==0):
					print("Resultado: ")
					self.vec.append(ss1)
					self.vec.append(ss2)
					print(ss1)
					print(ss2)
					return
				self.camino(M,i-1,j-1,ss1,ss2)

			if(M[i][j][1] == 1):
				#arriba
				ss1 += "-"
				ss2 += S2[i-1] 
				#print("arriba",i-1," ",j)
				if(i==0 or j==0):
					print("Resultado: ")
					self.vec.append(ss1)
					self.vec.append(ss2)
					print(ss1)
					print(ss2)
					return 
				self.camino(M,i-1,j,ss1,ss2)

			if(M[i][j][2] == 1):
				#costado
				ss1 += S1[j-1] 
				ss2 += "-"
				#print("costado",i," ",j-1)
				if(i==0 or j==0):
					print("Resultado: ")					
					self.vec.append(ss1)
					self.vec.append(ss2)
					print(ss1)
					print(ss2)
					return
				self.camino(M,i,j-1,ss1,ss2)

		elif(self.verificar(M,i,j) == 0):
			print("Resultado: ")
			self.vec.append(ss1)
			self.vec.append(ss2)
			print(ss1)
			print(ss2)

	def inciar(self,s1,s2,gapOpem): 

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


				pos_s1 = s1[j-1]
				pos_s2 = s2[i-1]
			#	print(pos_s1, pos_s2)
				
				#a = self.encontrar_valor(self.vec1, pos_s1)
				#b = self.encontrar_valor(self.vec2, pos_s2)

				value = self.identicalMatch
				
				if pos_s2 != pos_s1:
					value = self.mismatch  
			
				#print(v)
				
				f1 = M_vacia[i-1][j-1][3] + value
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
			
		print("////////Resultado1//////////")
		#print(M_vacia)
		#imprimir(M_vacia)
		print("***********************************************")
		i=3
		j=3
		ss1 = ""
		ss2 = ""

		self.camino(M_vacia,i,j,ss1,ss2)
	
	def empezar(self):
		self.inciar(self.S1,self.S2,self.gapOpem)
		return self.vec

	###############################################


	def get_sequences(self,F, i, j, alignmented_seq1 = "", alignmented_seq2 = ""):
		if F[i][j][0]==0:
			print("\t\t Alineamiento ")
			self.Solution.append(alignmented_seq1)
			self.Solution.append(alignmented_seq2)	
			#print (alignmented_seq1)
			#print (alignmented_seq2)	
			return
		if i > 0 or j > 0:			
			if (i>0 and j>0 and F[i][j][1] == 'D'):		
				alignmented_seq1 = self.S1[j-1] + alignmented_seq1
				alignmented_seq2 = self.S2[i-1] + alignmented_seq2
				i = i-1
				j = j-1
			elif (i>0 and F[i][j][1]=='U'):
				alignmented_seq1 = "-" + alignmented_seq2	
				alignmented_seq2 = self.S2[i-1] + alignmented_seq2
				i = i-1
			else:
				alignmented_seq2 = "-" + alignmented_seq2
				alignmented_seq1 = self.S1[j-1] + alignmented_seq1
				j = j-1
			self.get_sequences(F, i, j, alignmented_seq1, alignmented_seq2)	

	def local_alignment(self,F, i=1, j=1):
	
		row = self.row
		column = self.column

		value = self.identicalMatch
			
		if self.S1[i-1] != self.S2[j-1]:
			value = self.mismatch  


		diag = F[i-1][j-1][0] + value
		up = F[i-1][j][0] + self.gapOpem
		left = F[i][j-1][0] + self.gapOpem
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
			self.get_sequences(F, i, j)
			self.get_sequences(F, s_i, s_j)
			return
		if j<column-1:
			self.local_alignment(F, i ,j+1)	
		else:	
			self.local_alignment(F, i+1 ,1)

	def Alineamiento_Local(self):

		F = np.zeros([self.row, self.column], dtype='i,O') 
		self.local_alignment(F)


		print(len(self.Solution))

		return self.Solution


class Algoritmos_Distancia():





class Operadores():
	def inicio(request):
		return render(request,'Home.html')
		
	def PageOperador(request):
		tipo = request.POST['fase']
		#Tipo_Arbol = request.POST['arbol']

		#print(Alineamiento, Tipo_Arbol)
		#return render(request,'Thresholding.html',{"Algo":Alineamiento,"Arbol":Tipo_Arbol})


		if (tipo == "AlineamientoLocal") : 
			return render(request,'AlgoritmoAlineamiento.html',{"Algo":tipo})
		elif(tipo == "AlineamientoGlobal"):
			return render(request,'AlgoritmoAlineamiento.html',{"Algo":tipo})	
		elif(tipo == "Blast"):
			return render(request,'RaiseToPower.html',{"Algo":tipo})
		elif(tipo == "Muscle"):
			return render(request,'RaiseToPower.html',{"Algo":tipo})
		elif(tipo == "Jukes-cantor"):
			return render(request,'JudesCantor.html',{"Algo":tipo})	
		elif(tipo == "Kimura model"):
			return render(request,'RaiseToPower.html',{"Algo":tipo})	
		elif(tipo == "UPGMA"):
			return render(request,'RaiseToPower.html',{"Algo":tipo})
		elif(tipo == "Neighbor Joining"):
			return render(request,'RaiseToPower.html',{"Algo":tipo})

	def ControladorOperador(request):

		#id = request.POST['fase']
		tipo = request.POST['Tipo']
		'''myfile = request.FILES["file1"]
		myfile2 = request.FILES["file2"]
		print(myfile,myfile2)
		fs = FileSystemStorage()
		fs2 = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		filename2 = fs2.save(myfile2.name, myfile2)
		file_name = fs.url(filename)
		file_name2 = fs2.url(filename2)'''
		print(tipo)
		if(tipo == "AlineamientoLocal"):
			_gap = request.POST['gap']
			_match = request.POST['IdenticalMatch']
			_missMatch = request.POST['MissMatch']	

			_seq1 = request.POST['Seq1']
			_seq2 = request.POST['Seq2']	

			Algo_Alinamiento = 	Algoritmos2(_seq1,_seq2,int(_gap),int(_match),int(_missMatch))
			resultado = Algo_Alinamiento.Alineamiento_Local()
			return render(request,'ResulTOperador.html',{"labels2":tipo,"resultados": resultado} )	

		if(tipo == "AlineamientoGlobal"):
			_gap = request.POST['gap']
			_match = request.POST['IdenticalMatch']
			_missMatch = request.POST['MissMatch']	

			_seq1 = request.POST['Seq1']
			_seq2 = request.POST['Seq2']	

			Algo_Alinamiento = 	Algoritmos2(_seq1,_seq2,int(_gap),int(_match),int(_missMatch))
			resultado =  Algo_Alinamiento.empezar()
			return render(request,'ResulTOperador.html',{"labels2":tipo,"resultados": resultado} )	


		if(tipo == "Jukes-cantor"):

			_id1 = request.POST['id1']
			_id2 = request.POST['id2']
			_seq1 = request.POST['Seq1']
			_seq2 = request.POST['Seq2']	

			distancia = Algoritmos_Distancia()
			id, seq, d  =  distancia.main2(_id1,_seq1,_id2,_seq2)

			print(id,"\t", seq,"\t", d)
			return render(request,'resultadoJudes.html',{"labels2":tipo,"id": id,"seq":seq,"d":d} )	

	
		return render(request,'Home.html')



	