# Definición de variables iniciales
v_in = 5.0
I = 0.0001

# Se crean dos arreglos (listas) para almacenar los resultados por separado
lista_r1 = []
lista_r2 = []

# Solicitar al usuario el número total de voltajes a evaluar
cantidad_voltajes = int(input("¿Cuántos voltajes de salida desea calcular?: "))

# Ciclo principal para solicitar cada voltaje
for i in range(cantidad_voltajes):
    print(f"\n--- Evaluando voltaje #{i+1} ---")
    
    # Ciclo para validar que el voltaje ingresado sea correcto (0 < Vout < 5)
    while True:
        v_out = float(input("Ingrese el valor del voltaje de salida (Vout): "))
        
        if 0 < v_out < v_in:
            print("Voltaje válido. Calculando...")
            break # Rompe el ciclo while si el dato es correcto
        else:
            print(f"Error: El voltaje debe ser mayor a 0 y menor a {v_in}V. Intente de nuevo.")
    
    # Los cálculos de cada resistencia
    r1 = v_out / I
    r2 = (v_in - v_out) / I
    
    # Se agregan los valores calculados a sus respectivas listas
    lista_r1.append(r1)
    lista_r2.append(r2)
    
    print(f"Calculado: R1 = {r1} Ω, R2 = {r2} Ω")

# Imprimir los valores máximos y mínimos de las listas
print("\n=== RESUMEN DE RESISTENCIAS ===")
print(f"R1 -> Máxima: {max(lista_r1)} Ω | Mínima: {min(lista_r1)} Ω")
print(f"R2 -> Máxima: {max(lista_r2)} Ω | Mínima: {min(lista_r2)} Ω")