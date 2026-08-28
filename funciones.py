def calcular_resistencias_y_potencia(v_in, I, v_out):
    # Calcular los valores de resistencia en ohmios
    r1 = v_out / I
    r2 = (v_in - v_out) / I
    
    # Calcular la potencia real disipada en vatios (W)
    # Potencia = Voltaje en la resistencia * Corriente
    potencia_real_r1 = v_out * I
    potencia_real_r2 = (v_in - v_out) * I
    
    # Lógica para asignar la potencia nominal comercial
    def asignar_potencia_nominal(potencia_real):
        if potencia_real <= 0.25:
            return "1/4W"
        elif potencia_real <= 0.50:
            return "1/2W"
        elif potencia_real <= 1.0:
            return "1W"
        else:
            return "Mayor a 1W"
            
    nominal_r1 = asignar_potencia_nominal(potencia_real_r1)
    nominal_r2 = asignar_potencia_nominal(potencia_real_r2)
    
    # Retornar la lista con los 4 datos requeridos
    return [r1, r2, nominal_r1, nominal_r2]


# --- Ejemplo de cómo usarla 
v_in_prueba = 12
corriente_prueba = 0.05  # 50 mA
v_out_prueba = 5

resultado = calcular_resistencias_y_potencia(v_in_prueba, corriente_prueba, v_out_prueba)

print(f"R1: {resultado[0]} Ω ({resultado[2]})")
print(f"R2: {resultado[1]} Ω ({resultado[3]})")