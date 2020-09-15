#io_utilitiesIris

filepath = './iris.data'

with open(filepath,'r') as fp:
	data = fp.read()

dataLines = data.split('\n')
dataFinal = []

for line in dataLines:
	dataFinal.append(line.split(','))

print(dataFinal)