#Progrma que realiza la conversion de numeros binarios y numeros decimales version 0.1.1!

import os
binario = []
total = 0
class Miguel:
	def menu (self,):
		os.system("cls")
		print "*"*10
		print "BIENVENIDO"
		print "*"*10
		print"\n"*2
		print"Selecione una opcion \n\n","1)Convertir de Decimales a Binarios \n\n", 
		print "2)Convertir de Binarios a Decimales \n\n",

	def opc (self,):
		n = int(raw_input())
		#verificacion de la opcion
		if (n<0 or n>2): #verificacion del metodo 
			os.system("cls")
			print "error"
			print"\n"*10
			print"*"*30
			print"\n"*5
			os.system("pause")
		elif(n == 1): # en el primer caso el usuario selecciona convertir de decimales a binarios.
			os.system("cls")
			print "ingrese su numero decimal"
			deci = int(input())
			os.system("cls")
			print "la conversion de su numero decimal ",deci, " es ",bin(deci)
			print"\n"*5
			os.system("pause")
		else:
			os.system("cls")
			print "tiene conocimientos acerca de los numeros binarios\n"
			print "1)SI\n\n","2)NO \n\n"
			print "considere que de acuerdo a su respuesta se habilitara un servicio de ayuda \n"
			rpd=int(raw_input())
			if (rpd<0 or rpd>2): #verificacion del metodo 
				os.system("cls")
				print "error"
				print"\n"*10
				print"*"*30
				print"\n"*5
				os.system("pause")
			
			elif(rpd == 1): # en el primer caso el usuario conoce los numeros binarios se habilita el menu facil
				 int('1010001', 2)
				 os.system("cls")
				 print "ingrese su numero binario \n"
				 b = raw_input()
				 p = int(b,2)
				 print"*"*56
				 print "la conversion del numero binario es ",p 
				 print"*"*56
				 print"\n"*5
				 os.system("pause")
			else: # en este caso el usuario no conoce los numeros binarios se procede a realizar todo paso a paso 
				os.system("cls")
				n = int(raw_input("ingrese cuantos elementos posee su numero binario \n"))
				if (n<1):
					os.system("cls")
					print"el dato introducido es incorrecto \n"
					n = int(raw_input("ingrese cuantos elementos posee su numero binario \n"))
					os.system("cls")
				m=n-1
				for i in range(0,n):
					os.system("cls")
					print "ingrese su elemento", i+1
					elemento = int(raw_input())
					if (elemento < 0 or elemento >1):
						os.system("cls")
						print"su numero es incorrecto los numeros binarios poseen un rango del 0-1 \n""ingrese el elemento ", i+1
						elemento = int(raw_input())
						binario.append(elemento)
					else:
						binario.append(elemento)
				os.system("cls")
				total = 0
				for i in range(0,n):
					aux=binario[i]*2**m
					total = total + aux
					m=m-1
				os.system("cls")
				print "el numero binario que usted introdujo fue el siguiente \n"

				for i in range(0,n):
					print binario[i],
				print "\n"
				print "*"*56
				print "y la conversion de su numero binario ingresado es de ", total
				print "*"*56
				print"\n"*5
				os.system("pause")
					

m = Miguel()
m.menu()
m.opc()
