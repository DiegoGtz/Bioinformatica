from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.views.generic import CreateView
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import Storage
from django.core.files.base import ContentFile

#####################################################

import cv2 
import numpy as np
from matplotlib import pyplot as plt 
import	 math 

def inicio(request):
    return render(request,'Home.html')

class Algoritmos ():

	gap 		= 0 
	match 		= 0
	MissMatch	= 0
	Seq1 = "AAG"
	Seq2 = "AGC"
	column = len(Seq1)+1
	row = len(Seq2)+1
	Solution = []
   
   
	vec1 = {'A':0,'C':1,'G':2,'T':3}
	matrix_sus =  [[ 2,-7,-5,-7],
        		   [-7, 2,-7,-5],
        		   [-5,-7, 2,-7],
        		   [-7,-5,-7, 2]]



	def get_sequences(F, i, j, alignmented_seq1 = "", alignmented_seq2 = ""):
		if F[i][j][0]==0:
			print("\t\t Alineamiento ")
			Algoritmos.Solution.append(alignmented_seq1)
			Algoritmos.Solution.append(alignmented_seq2)	
			#print (alignmented_seq1)
			#print (alignmented_seq2)	
			return
		if i > 0 or j > 0:			
			if (i>0 and j>0 and F[i][j][1] == 'D'):		
				alignmented_seq1 = Algoritmos.Seq1[j-1] + alignmented_seq1
				alignmented_seq2 = Algoritmos.Seq2[i-1] + alignmented_seq2
				i = i-1
				j = j-1
			elif (i>0 and F[i][j][1]=='U'):
				alignmented_seq1 = "-" + alignmented_seq2	
				alignmented_seq2 = Algoritmos.Seq2[i-1] + alignmented_seq2
				i = i-1
			else:
				alignmented_seq2 = "-" + alignmented_seq2
				alignmented_seq1 = Algoritmos.Seq1[j-1] + alignmented_seq1
				j = j-1
			Algoritmos.get_sequences(F, i, j, alignmented_seq1, alignmented_seq2)			

	def local_alignment(F, i=1, j=1):
	
		row = Algoritmos.row
		column = Algoritmos.column
		diag = F[i-1][j-1][0] + Algoritmos.matrix_sus[Algoritmos.vec1[Algoritmos.Seq2[i-1]]][Algoritmos.vec1[Algoritmos.Seq1[j-1]]]
		up = F[i-1][j][0] + Algoritmos.gap
		left = F[i][j-1][0] + Algoritmos.gap
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
			Algoritmos.get_sequences(F, i, j)
			Algoritmos.get_sequences(F, s_i, s_j)
			return
		if j<column-1:
			Algoritmos.local_alignment(F, i ,j+1)	
		else:	
			Algoritmos.local_alignment(F, i+1 ,1)



	def Alineamiento_Local(self,gap,Identical_Match,Miss_Match,seq1,seq2):
		Algoritmos.gap = gap
		Algoritmos.match =  Identical_Match
		Algoritmos.Miss_Match = Miss_Match


		F = np.zeros([Algoritmos.row, Algoritmos.column], dtype='i,O') 
		Algoritmos.local_alignment(F)


		print(len(Algoritmos.Solution))






class Operadores():
	def inicio(request):
		return render(request,'Home.html')
		
	def PageOperador(request):
		Alineamiento = request.POST['fase']
		Tipo_Arbol = request.POST['arbol']

		#print(Alineamiento, Tipo_Arbol)
		return render(request,'Thresholding.html',{"Algo":Alineamiento,"Arbol":Tipo_Arbol})

		'''if(tipo == "Thresholding"):
			return render(request,'Thresholding.html',{"labels":tipo})
		elif(tipo == "Outlier_C.Stretching"):
			return render(request,'Outlier_Contrast_Stretching.html',{"labels":tipo})	
		elif(tipo == "Contrast_stretching"):
			return render(request,'Contrast_stretching.html',{"labels":tipo})		
		elif(tipo == "E.Histograma"):
			return render(request,'Ecualizacion_Histograma.html',{"labels":tipo})
		elif(tipo == "O.Logaritmico"):
			return render(request,'PageOperador.html',{"labels":tipo})
		elif(tipo == "O.Raiz"):
			return render(request,'PageOperador.html',{"labels":tipo})
		elif(tipo == "O.Exponencial"):
			return render(request,'Operador_Exponencial.html',{"labels":tipo})	
		elif(tipo == "O.RaiseToPower"):
			return render(request,'RaiseToPower.html',{"labels":tipo})
		elif(tipo == "Cascada"):

			return render(request,'Cascada.html',{"labels":tipo})		

		elif(tipo == "Add"):

			return render(request,'Addition.html',{"labels":tipo})	
		elif(tipo == "Subtraction"):
			return render(request,'Subtraction.html',{"labels":tipo})	

		elif(tipo == "Multiplicacion" ):
			return render(request,'Multiplicacion.html',{"labels":tipo})
		elif(tipo == "Blending" ):
			return render(request,'Blending.html',{"labels":tipo})
		elif(tipo == "Division" ):
			return render(request,'Division.html',{"labels":tipo})'''
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

			Algo_Alinamiento = 	Algoritmos()
			resultado =  Algo_Alinamiento.Alineamiento_Local(int(_gap), int(_match), int(_missMatch), _seq1, _seq2)
			return render(request,'ResulTOperador.html',{"labels2":tipo} )	


		'''#print(file_name,file_name2)
		if(tipo == "Thresholding"):
			min1 = request.POST['min']
			max2 = request.POST['max']			
			resultado =  Algoritmos.Thresholding(file_name,int(min1),int(max2))
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )

		if(tipo == "Outlier_C.Stretching"):
			a = request.POST['a']
			b = request.POST['b']
			Low = request.POST['Low']
			Max = request.POST['Max']
			resultado = Algoritmos.Outlier_Contrast_Stretching(file_name,int(a),int(b),int(Low),int(Max))

			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if(tipo == "Contrast_stretching"):
			a = request.POST['a']
			b = request.POST['b']
			resultado = Algoritmos.Contrast_Stretching(file_name,int(a),int(b))

			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )

		if(tipo == "E.Histograma"):
			resultado = Algoritmos.ecualizacion_histograma(file_name)

			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if(tipo == "O.Logaritmico"):
			c = request.POST['c']
			resultado = Algoritmos.operador_logaritmo(file_name,int(c))

			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )

		if(tipo == "O.Raiz"):
			c = request.POST['c']
			resultado = Algoritmos.operador_Root(file_name,int(c))

			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if(tipo == "O.Exponencial"):
			c = request.POST['c']
			b = request.POST['b']
			
			resultado = Algoritmos.operador_Exponencial(file_name,float(c),float(b))
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )	
		if(tipo == "O.RaiseToPower"):
			c = request.POST['c']
			r = request.POST['r']
			
			resultado = Algoritmos.operador_Raise_to_power(file_name,float(c),float(r))
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if(tipo == "Cascada"):

			a,b = 0 , 255 
			Resultado1 =  Algoritmos.Contrast_Stretching(file_name,a,b)
			Resultado2 = Algoritmos.ecualizacion_histograma(file_name)
			c = 70 
			Resultado3 = Algoritmos.operador_logaritmo(file_name,c)
			c =20
			Resultado4 = Algoritmos.operador_Root(file_name,c)
			c,b = 20 , 1.01
			Resultado5 = Algoritmos.operador_Exponencial(file_name,c,b)
			c, r = 0.1 , 1.5
			Resultado6 = Algoritmos.operador_Raise_to_power(file_name,c,r)

			return render(request,'Resultado_Cascada.html',{"labels2":tipo,
				"image":"/"+Resultado1,
				"image2":"/"+Resultado2,
				"image3":"/"+Resultado3,
				"image4":"/"+Resultado4,
				"image5":"/"+Resultado5,
				"image6":"/"+Resultado6,
				} )		


		if (tipo == "Add"):
			#return render(request,'Home.html')
			resultado = Algoritmos.pixel_adition(file_name,file_name2)
		
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if (tipo == "Subtraction"):

			resultado = Algoritmos.pixel_sustraction(file_name,file_name2)
			
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if (tipo == "Multiplicacion"):
			c = request.POST['c']
			resultado = Algoritmos.multiplication(file_name,int(c))
		
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if (tipo == "Blending"):
			#return render(request,'Home.html')
			x = request.POST['x']

			resultado = Algoritmos.blending(file_name,file_name2,float(x))
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if (tipo == "Division"):
			#return render(request,'Home.html')
			resultado = Algoritmos.pixel_division(file_name,file_name2)
		
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		'''
		return render(request,'Home.html')



	