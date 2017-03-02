import numpy as np

def cargarArchivo(nombre, separador, hayStr=False, numero=0):
	data = {}
	lines = open(nombre, 'r').readlines()
	np.random.shuffle(lines)
	for line in lines:
		i = 0
		for word in line.split(separador):
			if not hayStr or i != numero:
				word = float(word) 

			try:
				data[i].append(word)
			except:
				data[i] = []
				data[i].append(word)

			i += 1

	print("len de data[0]: ",len(data[0]))
	print("data[0]",data[0])
	return data

def backpropagation(numCapas, numSalidas, numNeuronas, data):
	# Numero de entradas
	n = len(data) - 1
	pesosEntradaHidden = []
	pesosHiddenSalida = []

	for i in range(n):
		pesosEntradaHidden.append(np.random.randint(low=-0.5,high=0.5,size=numCapas)) # ¿No debería ser numNeuronas en vez de numCapas?

	for i in range(numSalidas):
		pesosHiddenSalida.append(np.random.randint(low=-0.5,high=0.5,size=numNeuronas)) # Creo que debería ir así, no estoy claro

	# No sé si te cuadra
	if numCapas > 1:
		pesosHiddenHidden = []
		for i in range(numCapas):
			tmp = []
			tmp.append(np.random.randint(low=-0.5,high=0.5,size=numNeuronas))
			pesosHiddenHidden.append(tmp)

	print("pesosEntradaHidden: ", pesosEntradaHidden)
	print("pesosHiddenSalida: ", pesosHiddenSalida)
	print("pesosHiddenHidden: ", pesosHiddenHidden)

def main():
	primero = cargarArchivo('500.txt', ' ')
	#segundo = cargarArchivo('1000.txt', ' ')
	#tercero = cargarArchivo('2000.txt', ' ')
	backpropagation(3, 1, 4, primero)
	#print(a)
	#b = cargarArchivo('iris-data.txt', ',', True, 4)
	#print(b)

if __name__ == '__main__':
	main()