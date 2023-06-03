saldo_inicial = 3000
saldoactual= saldo_inicial

def retirar():
    monto = int(input("Ingrese monto a retirar: "))
    if monto > saldo_inicial: 
        print("no puede retirar esa cantidad, saldo insuficiente")
        return menu()
    if  monto <= saldo_inicial: 
        global saldoactual
        saldoactual = saldo_inicial - monto 
        print(f'retiro de  fondos exitoso!, saldo actual:{saldoactual}')
        return menu()


def saldo():
    global saldoactual
    print(f'su saldo es: {saldoactual}')
    return menu()
    

def depositar():
    monto = int(input("ingrese cantidad a depositar: "))
    global saldoactual
    saldoactual = saldo_inicial + monto
    print (f'ingreso exitoso, saldo actual: {saldoactual}')
    return menu()

def menu():
    print("------BIENVENIDO---------")
    print("1- retirar efectivo")
    print("2- ver saldo actual")
    print("3- depositar")
    print("4- salir")
    opcion = input("ingrese una opcion: ")

    match opcion:
        case "1": retirar()
        case "2": saldo()
        case "3": depositar()

menu()

    



