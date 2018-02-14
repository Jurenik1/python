

def imprimir():
	print "mi primera funcion"
	

def funcion():
	return "Hola mundo"

	
#def par_impar(num):
#	if num%2==0:
#		return "par"
#	else:
#		return "impar"
		

def par_impar1(num):
	return "par" if (num%2==0) else "impar"
	

def datos (dni, nombre, *apellidos):
	print dni
	print nombre
	print "Tienes"+str(len(apellidos))+" apellidos"
	for argumento in apellidos:
		print argumento
