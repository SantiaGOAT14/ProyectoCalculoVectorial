from sympy import symbols, Eq, solve, diff

# Declaramos las variables y los parámetros
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

# Resolvemos el sistema de ecuaciones para encontrar los valores óptimos de x y y
critical_points = solve((dV_dx, dV_dy), (x, y))

# Calculamos h para los valores óptimos de x y y
optimal_solutions = []
for point in critical_points:
    x_val, y_val = point
    h_val = h_expr.subs({x: x_val, y: y_val})
    V_val = V.subs({x: x_val, y: y_val, h: h_val})
    optimal_solutions.append({'x': x_val, 'y': y_val, 'h': h_val, 'V': V_val})

# Imprimimos los resultados
for solution in optimal_solutions:
    print(f"Optimal dimensions:")
    print(f"  x = {solution['x']}")
    print(f"  y = {solution['y']}")
    print(f"  h = {solution['h']}")
    print(f"  Maximum Volume = {solution['V']}")
