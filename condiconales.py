#Solicitamos el voltaje inicial
vin = abs(float(input("Ingrese el valor del voltaje inicial: \n")))

#Solicitamos el tamaño de la primera resistencia
r1 = abs(float(input("Ingrese el valor de la primera resistencia: \n")))

#Solicitamos los Watts de la primera resistencia
r1_w = abs(int(input("Seleccione la potencia de esta resistencia: \n 1:1/4W \n 2:1/2W \n 3:1W \n")))

if r1_w == 1 or r1_w == 2  or r1_w == 3:
    print("La resistencia opera dentro del rango establecido de potencia \n")
else:
     print("La resistencia no cumple con el rango establecido de potencia \n")

#Solicitamos el tamaño de la segunda resistencia
r2 = abs(float(input("Ingrese el valor de la segunda resistencia: \n")))

#Solicitamos los Watts de la segunda resistencia
r2_w = abs(int(input("Seleccione la potencia de esta resistencia: \n 1:1/4W \n 2:1/2W \n 3:1W")))

if r2_w == 1 or r2_w == 2  or r2_w == 3:
    print("La resistencia opera dentro del rango establecido de potencia")
else:
     print("La resistencia no cumple con el rango establecido de potencia")


divisor = ((vin*r1)/(r1+r2))

print("El valor de voltaje recibido en la primera resistencia es de: ",divisor)
print("El valor de voltaje recibido en la segunda resistencia es de: ", vin-divisor)
print("La corriente que circula por el circito es de: ", (vin)/(r1+r2), "A")