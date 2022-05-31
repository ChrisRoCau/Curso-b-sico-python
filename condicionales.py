#Declaramos una variable 

calificacion = input("Introduce tu calificación de la AZ900: ")

calificacion = int(calificacion)

#Preguntamos si la calificación es menor a 700

if calificacion < 700:
    print("Veeees, por no estudiar")

elif calificacion > 1000:
    print("Mientees!!!! no puedes sacar más de mil")
else: #Si no se cumple el if anterior, pasa a esta linea
    print("Felicidades, pasa por tu certificado")

#Verificador de Edad

edad = input("Intruduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100:
    print("Bienvenid@ a mamitas")
elif edad > 100:
    print("Si vienes acompañad@ de tus abuelitos , si te podemos fiar") 
elif edad < 0:
    print("Ni que fueras viajer@ del tiempo")
else:
    print("No puedes llevarte esos cigarros")

#En python no hay switch case