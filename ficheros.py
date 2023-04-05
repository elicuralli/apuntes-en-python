#fichero = open('mitexto.txt', 'w')
#fichero.write('hola mundo')

class Vehiculo:

    def __init__(self, color, puertas,marca, modelo):
        self.color = color
        self.puertas = puertas
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f' el vehiculo es de marca {self.marca}, modelo {self.modelo} de color {self.color} y tiene {self.puertas} puertas'


carro = Vehiculo(marca= "chevrolet", modelo = 'aveo', color="verde",puertas= "4")
#print(carro)

