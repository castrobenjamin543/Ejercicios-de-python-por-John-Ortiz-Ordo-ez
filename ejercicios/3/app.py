# mostrar la fecha y hora actual

import datetime

ahora = datetime.datetime.now()

print(ahora)

#formateo del tiempo

# En este caso solamente mostramos la fecha y hora sin los milisegundos

print(ahora.strftime('%d/%m/%y %H:%M:%S'))
