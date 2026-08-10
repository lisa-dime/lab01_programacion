#Definicion de variables y arreglos
v_in = 5
I = 0.0001
resistences = []
v_out = 0
r1 = v_out/I
r2 = (v_in-v_out)/I
#Ciclo para validar el valor de voltaje de salida (Valor entre 0 y 5)
while True:
    v_out = float(input("Ingrese el valor del voltaje de salida: \n"))
    if v_out < 5  and v_out > 0:
        print("El valor de voltaje de salida es correcto")
        break
    print("El valor de voltaje de salida debe ser mayor a 0 y menor a ", v_in, "V")
#Se agregan los valores de resistencia al arreglo   
resistences.append(r1)
resistences.append(r2)
#Se imprimen los valores de resistencia maxima y minima
print("Resitencia maxima: ", max(resistences), "Ω" , "\n Resistencia Minima: ", min(resistences), "Ω" )

