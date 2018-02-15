

def gordos(directorio,size):
        if size[-1:].upper() not in ('K','M','G'):
                print "Solo K,M,G"
        tam=int(size[0:-1])
        if size[-1:].upper()=='K':
                bytes=tam*1024
        elif size[-1:].upper()=='M':
                bytes=tam*1024*1024
        else:
                bytes=tam*1024*1024*1024

        lista=os.listdir(directorio)
        for fichero in lista:
                if os.path.getsize(directorio+"/"+fichero)> bytes:
                        print fichero+" "+ str(os.path.getsize(directorio+"/"+fichero))

def version():
	return 1.0

def crea_dir(directorio)
	if os.access (directorio, 0):
		print "El directorio ya existe"
	else:
		os.mkdir(directorio)

def entorno()
	for x,y in os.environ.iteritems():
		if x=="USER" or x=="PATH" or x=="SHELL"
			print x
	
	
def visualizar (fichero):
	if not os.access(fichero,0):
		print "Fichero no existe"
		return False
	f=open('fichero','r')
	while True:
		linea = f.readLine()
		if not linea:break
		print (linea[0:-1])
