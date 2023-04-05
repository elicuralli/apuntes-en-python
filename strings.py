#f-strings 
#format %

nombre='elibeth'
edad='20'

#print('hola soy, %s y mi edad es %s'%(nombre,edad))

#print('hola soy, {} y mi edad es {}'.format(nombre,edad))

#print(f'hola soy {nombre} y mi edad es {edad}')

class Student:
    def __init__(self,nombre,apellido,edad):
        self.nombre =nombre
        self.apellido = apellido
        self.edad= edad

    def __str__(self):
        return f'hola soy {self.nombre} {self.apellido} y mi edad es {self.edad}'
    
new_student=   Student('elibeth','curalli',20)
#print(f'{new_student}')

mitexto="hola MundO"
mitexto.capitalize()# coloca solo la 1era letra en mayus
#print(mitexto.title())#coloca las primeras letras en mayus
mitexto.upper()#todo mayus
mitexto.replace('a','o')#reemplaza a por o
mitexto.find('hola')#dice la posicion donde se encuentra ese string en caso q exista

mitexto.lower()#coloca minus
mitexto.split()#transforma de string a lista

a='hola esto es un string'
b=['hola','soy','una','lista']
c=' '
#print(c.join(b)) #de esta forma transformo de lista a string uniendo la lista a un string vacio con 1 espacio
#print(a.split())
mitexto.isnumeric()#es false si es texto true si hay numeros en ese string

#(f'esto es para mostrar solo dos decimales al imprimir un resultado de una variable o formula por ejemplo'{variable:.2f})
