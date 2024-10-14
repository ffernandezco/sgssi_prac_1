import hashlib
import os

def encontrar(archivo):
	with open(archivo, "rb") as f:
		datos = f.read()
		hash_md5 = hashlib.new("md5")
		hash_md5.update(datos)
		return hash_md5.hexdigest()

carpeta = "/home/francisco/Desktop/lab1.2/imagen/"
lista_archivos = os.listdir(carpeta)
encontrado = False
indice = 0

while encontrado == False and indice < len(lista_archivos):
	archivo = lista_archivos[indice]
	archivo = carpeta + os.sep + archivo
	if os.path.isfile(archivo):
		valor_hash = encontrar(archivo)
		if(valor_hash == "e5ed313192776744b9b93b1320b5e268"):
			encontrado = True
			print("El archivo con el hash indicado es " + archivo)
	indice = indice + 1

