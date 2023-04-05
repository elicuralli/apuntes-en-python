#inconcluso da error en linea 27

class Perro:
    pass
    def __init__(self,nombre,raza):
        self.nombre = nombre
        self.raza = raza
    
    def descripcion(self):
        return '{} es un perro de raza: {}'.format(self.nombre,self.raza)
    
class Mascota(Perro):
    def ladra(self,ladrabastante):
        return '{} ladrido: {}'.format(self.nombre,ladrabastante)


nuevo_perro= Mascota('luna','mestiza')
#print(nuevo_perro.descripcion())
#print(nuevo_perro.ladra('ladra bastante'))

class Calculadora:
    def __init__(self,num):
        self.n = num
        self.datos = [0 for i in range(num)]
    
    def ingresar_dato(self):
        self.datos = [int(input('ingresar datos'str(i+1) + '= '))for i in range(n)]
    
    class Operacion(Calculadora):
        def __init__(self):
            Calculadora.__init__(self,2)
        
        def suma(self):
            a,b = self.datos
            s= a+b 
            print('el resultado es: ',s)
        
        def resta(self):
            a,b = self.datos
            r= a-b 
            print('el resultado es: ',r)

    