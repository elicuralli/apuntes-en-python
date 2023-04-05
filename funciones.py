annio=int(input('ingresa un año: '))
def bisiesto():
    if (annio %4==0 and annio %100 !=0) or (annio %400==0):
        print("el año: ", annio, "es bisiesto")
    else:
        print("el año: ", annio, " no es bisiesto")

bisiesto()