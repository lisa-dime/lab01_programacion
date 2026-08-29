from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

# 1. Inicializar el circuito
circuit = Circuit('Divisor de Voltaje')

voltaje = float(input("Ingrese el voltaje de entrada (V): "));
r1 = float(input("Ingrese el valor de la resistencia R1 (Ohm): "));
r2 = float(input("Ingrese el valor de la resistencia R2 (Ohm): "));

# 2. Agregar los componentes
circuit.V('fuente', 'in', circuit.gnd, voltaje)
circuit.R(1, 'in', 'out', r1)
circuit.R(2, 'out', circuit.gnd, r2)

# 3. Configurar el simulador
simulator = circuit.simulator()

# Ejecutar un análisis de Punto de Operación (DC)
analysis = simulator.operating_point()

# 4. Extraer e imprimir los resultados
v_in = float(analysis['in'][0])
v_out = float(analysis['out'][0])
vr1= float(analysis['in'][0]) - float(analysis['out'][0]) 

print(f"Voltaje de R1 (Vin): {vr1:.2f} V")
print(f"Voltaje de R2 (Vout): {v_out:.2f} V")