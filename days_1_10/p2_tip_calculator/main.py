"""
Instrucciones para el proyectos 2: Tip Calculator

Vamos a construir una calculadora de propinas.

Si la cuenta fue de $150.00, dividida entre 5 personas, con un 12% de propina.

Cada persona debería pagar:

(150.00 / 5) * 1.12 = 33.6

Después de formatear el resultado a 2 decimales = 33.60
"""
print("Bienvenido a la calculadora de propinas.")
cuenta = float(input("¿Cuál es el total de la cuenta? $: "))
propina = int(input("¿Cuánta propina quieres dar? 10, 12 o 15? "))
personas = int(input("¿Cuántas personas van a dividir la cuenta? "))
cuenta_por_persona = round((cuenta / personas) * (1 + propina / 100),2)

print(f"Cada persona debería pagar: ${cuenta_por_persona}")