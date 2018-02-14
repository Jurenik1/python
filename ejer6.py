# -*- coding: utf-8 -*-

# método count

import os
lista=os.listdir("c:\windows\system32")
letra = raw_input("Escriba un letra: ")
contador=[]
for y in lista:
	if y.count(letra) >0:
		contador.append(y)
		print y
			
print "hay "+str (len(contador)) + "en la lista con esta letra"