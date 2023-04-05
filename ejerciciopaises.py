"""
Crea un script que le pida al usuario una lista de países (separados por comas). 
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
"""

pais =input("ingrese una lista de paises separados por coma: ")

res = pais.split(",")#string a lista con split
res2 = set(res) #set para que no existan elementos repetidos        
#print(sorted(res2)) #se imprimen de forma alfabetica



