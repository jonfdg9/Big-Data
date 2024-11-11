import matplotlib.pyplot as plt

#Ejercicio 1B
options = [1,2,3,4,5,6]
count = [5,15,20,10,8,2]
plt.pie(count, colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"], labels = options, autopct = "%0.2f%%")
plt.title("Nº personas en familia")
plt.show()

#Ejercicio 1C
options = ["1","2","3","4","5","6","6+"]
count = [5,15,20,10,8,2,0]
plt.bar(options, count)
plt.xlabel("Nº personas")
plt.ylabel("Nº familias")
plt.title("Nº personas en familia")
plt.show()


#Ejercicio 11
options = ["[0  ,5) ","[5 , 10)","[10 , 15)","[15 ,20) "]
count = [3,8,5,4]
plt.bar(options, count)
plt.show()