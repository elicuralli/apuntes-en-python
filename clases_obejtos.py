# clases y objetos, metodos

class Matematica:
    def suma(self):
        self.num1= 2
        self.num2= 3

sumar= Matematica()
sumar.suma()
#print(sumar.num1+sumar.num2)

class Ropa:
    def __init__(self):
        self.marca = 'berska'
        self.talla ='u'
        self.color = 'rojo'

vestido = Ropa()
#print(vestido.color,vestido.talla,vestido.marca)

class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1+n2
        self.resta=  n1 - n2
        self.producto = n1*n2
        self.division = n1/n2

operacion = Calculadora(2,5)
#print(operacion.suma)

#clases y objetos bootcamp

class Juguete:
    _encendido = True
   
    def __init__(self,x):
        print('estoy en en el constructor de la clase juguete',x)
    
    def enciende(self):
        self._encendido = True
    
    def apaga(self):
        self._encendido = False

    def isEncendido(self):
        return self._encendido

class Dino(Juguete):
    color = None
    nombre = None

    def __init__(self, nombre):
        super().__init__(nombre)
        print('estoy en el constructor de la clase dino')
        
    def ver_escama(self):
        pass

#d = Dino('midino')
#d.enciende()
#print(d.isEncendido())
#d.apaga()
#print(d.isEncendido())


# inicializamos la clase
class Vehiculo():
    # inicializamos los atributos
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas, self.puertas )

class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} puertas, {} cc".format( self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada )

# bloque principal
# creamos el nuevo objeto, lo inicializamos y se imprime
coche = Coche("azul", 4, 4, 150, 1200)
#print(coche)

class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print(nombre)
    
    def Notas(self):
        if self.nota>=10: 
            print(' Aprobado')
        else:
            if self.nota<=10:
                print('Reprobado')
        
#a= Alumno('maria', 10)
#print('tu calificacion es: ',a.nota)
#print(a.Notas())


#solucioon al ejercicio
# inicializamos la clase
class Alumno:
    # inicializamos los atributos
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
 
 
    # función para imprimir los datos
    def imprimir(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)
 
 
    # función para obtener el resultado
    def resultado(self):
            if self.nota < 5:
                print("El alumno ha suspendido")
            else:
                print("El alumno ha aprobado")
 
 
 
# bloque principal
# creamos los nuevos objetos
#alumno1=Alumno()
#alumno2=Alumno()
 
# inicializamos los atributos
#alumno1.inicializar("María",8)
#alumno2.inicializar("Pepe",4)
 
# imprimimos los datos y resultados de cada alumno
#alumno1.imprimir()
#alumno1.resultado()
#alumno2.imprimir()
#alumno2.resultado()

       