import math as m
num = int(input("Cuantos valores distintos vas a añadir? "))
n=0
media=0
colec={}
for i in range(num):
    valor = int(input("Introduce el valor: "))
    cant = int(input("Cuantas veces esta: "))
    colec[valor]=cant
    n+=cant
    media+=valor*cant

media=media/n


sumatorio=0
for i in (colec):
    sumatorio+=((i-media)**2)*colec[i]
    print(i)

print (f"La media es: {media}")
print(f"La varianza es:{sumatorio/n} y la desviacion es: {m.sqrt(sumatorio/n)}")

