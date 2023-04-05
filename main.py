import operaciones 

def main():
    print("Esto es una calculadora ingrese dos numeros a operar")
    a= int(input("ingrese un numero: "))
    b= int(input("ingrese otro numero: "))
    c = operaciones.suma(n1= a,n2=b)
    d= operaciones.resta(n1 =a, n2=b)
    e = operaciones.multiplicar(n1=a, n2=b)
    print("el resultado de la suma es: ",c)
    print("el resultado de la resta es: ",d)
    print("el resultado de la multiplicacion es: ",e)

#main()

funcion = lambda n1, n2: n1**n2
#print(funcion(5,5))

def saludar(**nombres):

    print(nombres) # vemos como tenemos un diccionario en el parámetro nombres

    for parametro in nombres:
        print(f'¡Hola, {nombres[parametro]}!')

#print(saludar(nombre1= 'maria',nombre2= 'laura',nombre3= 'victor'))

