import numpy as np

def enCirculo(x,y):
	res = ((x - 10) ** 2) + ((y - 10) ** 2)

	if res <= 36:
		valor = 1
	else:
		valor = 0

	return valor

def genPoints(cantPuntos):
	ceros = 0
	archivo = open(str(cantPuntos)+"-generados.txt", 'w')

	mitad = (cantPuntos / 2)
	i = 0
	while i < cantPuntos:
		x = np.random.uniform(0,20)
		y = np.random.uniform(0,20)
		valor = enCirculo(x,y)
		if ceros == mitad and valor == 0:
			continue
		if valor == 0:
			ceros += 1
		if i == cantPuntos - 1:
			archivo.write(str(x) + ' ' + str(y) + ' ' + str(valor))
		else:
			archivo.write(str(x) + ' ' + str(y) + ' ' + str(valor) + '\n')
		i += 1
	
	archivo.close()

def main():
	genPoints(500)
	genPoints(1000)
	genPoints(2000)

if __name__ == '__main__':
	main()			