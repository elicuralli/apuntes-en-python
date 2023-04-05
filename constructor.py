class Persona:
    pass
    def __init__(self,nombre,year):
        self.nombre = nombre
        self.year = year
    
    def descripcion(self):
        return '{} tiene {}'.format(self.nombre,self.year)
    
    def comentario(self,frase):
        return '{} dice {}'.format(self.nombre,frase)

doctor = Persona('elibeth',20)
#print(doctor.descripcion())
#print(doctor.comentario('hola bb'))

#modificar un atributo

class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

correo = Email()
print(correo.enviado)
correo.enviar_correo()
print(correo.enviado)