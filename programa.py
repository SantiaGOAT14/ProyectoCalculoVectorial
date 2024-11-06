from multiprocessing.spawn import _main
from sympy import symbols, Eq, solve, diff

# Declaramos las variables
x, y, h, A_total = symbols('x y h A_total')

# Definimos la función de volumen y la restricción de área
V = x * y * h
area_constraint = Eq(2 * (x * y + x * h + y * h), A_total)

# Usamos la restricción para expresar h en términos de x, y y A_total
h_expr = solve(area_constraint, h)[0]

# Reemplazamos h en la función de volumen
V_sub = V.subs(h, h_expr)

# Calculamos las derivadas parciales de V_sub respecto a x y y
dV_dx = diff(V_sub, x)
dV_dy = diff(V_sub, y)

def calcular():
    """summary Función que inicializa un programa que maximiza el volumen de una caja
        Se solicitan datos al usuario para saber el área total de la superficie
    """
    
    try:
        print("-------------------------------------------------")
        print("Programa para maximizar el volumen de una caja")
        print("-------------------------------------------------")
        
        # Solicitamos al usuario el área total de la superficie
        A_total_value = float(input("Ingrese el área total de la superficie: "))
        
        # Verificamos que el valor ingresado sea positivo y suficiente para construir una caja
        if A_total_value <= 0:
            print("Error: El área total debe ser un número positivo mayor que cero.")
            return

        # Sustituimos el valor de A_total en las derivadas parciales
        dV_dx_num = dV_dx.subs(A_total, A_total_value)
        dV_dy_num = dV_dy.subs(A_total, A_total_value)

        # Resolvemos el sistema de ecuaciones con el valor numérico de A_total
        critical_points = solve((dV_dx_num, dV_dy_num), (x, y))

        # Calculamos h para los valores óptimos de x y y con el valor numérico de A_total
        optimal_solutions = []
        for point in critical_points:
            x_val, y_val = point
            h_val = h_expr.subs({x: x_val, y: y_val, A_total: A_total_value})
            
            # Filtramos las soluciones para asegurarnos de que sean todas positivas
            if x_val > 0 and y_val > 0 and h_val > 0:
                V_val = V.subs({x: x_val, y: y_val, h: h_val})
                optimal_solutions.append({
                    'x': x_val.evalf(), 
                    'y': y_val.evalf(), 
                    'h': h_val.evalf(), 
                    'V': V_val.evalf()
                })

        # Verificamos si se encontraron soluciones válidas
        if not optimal_solutions:
            print("No se encontraron soluciones válidas con el área proporcionada. Intente con un área mayor.")
            return

        # Imprimimos los resultados de forma más clara
        print("\nDimensiones óptimas y volumen máximo:")
        for i, solution in enumerate(optimal_solutions, start=1):
            print(f"Solución {i}:")
            print(f"  x = {solution['x']:.2f}")
            print(f"  y = {solution['y']:.2f}")
            print(f"  h = {solution['h']:.2f}")
            print(f"  Volumen máximo = {solution['V']:.2f}")
            print("-" * 30)

    except ValueError:
        print("Error: Por favor, ingrese un número válido para el área total.")
        
def main():
    """summary Función principal que ejecuta el programa
    """
    while True:
        # Función que obtiene los volumenes
        calcular()

        # Preguntar si quiere volver a calcular
        repeat = input("¿Desea calcular otro volumen? (S/N): ").lower()
        
        # Si el usuario elige "no", salimos del bucle
        if repeat != "s":
            print("Fin del programa")
            break

# Ejecutamos la función principal
if __name__ == "__main__":
    main()
