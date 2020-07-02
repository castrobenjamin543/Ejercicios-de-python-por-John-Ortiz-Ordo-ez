#pedir por teclado el radio de un circulo y mostrar el area dd dicho circulo

from math import pi

r = float(input("Ingresa el radio de un circulo: "))

area = pi * r ** 2;

print("El area del circulo es: {}".format(area) )