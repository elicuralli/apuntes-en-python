saldo_inicial = 3000

def menu():
    print("------BIENVENIDO---------")
    print("1- retirar efectivo")
    print("2- ver saldo actual")
    print("3- depositar")
    print("4- salir")

def retirar():
    monto = int(input("Ingrese monto a retirar: "))
    if monto > saldo_inicial: 
        print("no puede retirar esa cantidad, saldo insuficiente")
    if  monto <= saldo_inicial: 
        saldoactual = saldo_inicial - monto 
        print(f'retiro de  fondos exitoso!, saldo actual:{saldoactual}')


def saldo():
    print(f'su saldo es: {saldo_inicial}')
    

def depositar():
    monto = int(input("ingrese cantidad a depositar: "))
    saldoactual = saldo_inicial + monto
    print (f'ingreso exitoso, saldo actual: {saldoactual}')
    

menu()
opcion = input("ingrese una opcion: ")

match opcion:
    case "1": retirar()
    case "2": saldo()
    case "3": depositar()
    



