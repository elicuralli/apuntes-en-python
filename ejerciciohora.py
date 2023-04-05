import time 

hora= time.strftime('%H')
minutos = time.strftime('M')


if int(hora)>=7:
    print('es hora de irse')
else:
    print('Quedan {} horas y {} minutos restantes para irse'.format(18 - int(hora), 59-int(minutos)))