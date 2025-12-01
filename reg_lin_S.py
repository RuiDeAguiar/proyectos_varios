import pandas as pd
import statsmodels.api as sm

# 1. CREAR LOS DATOS (Simulación)
# Imaginemos que estos son tus datos ya limpios en un DataFrame
data = {
    'Exceso_Mercado_X': [1.5, 2.0, -1.0, 3.5, 0.5, -2.0, 2.5, 1.0],  # Rm - Rf
    'Exceso_Activo_Y':  [1.8, 2.3, -0.8, 4.1, 0.7, -2.5, 2.9, 1.3]   # Ri - Rf
}

df = pd.DataFrame(data)

# 2. DEFINIR X e Y
# Y = Variable Dependiente (Lo que queremos explicar)
Y = df['Exceso_Activo_Y']

# X = Variable Independiente (El predictor)
X = df['Exceso_Mercado_X']

# 3. AGREGAR LA CONSTANTE (El Intercepto / Alpha)
# ¡OJO! statsmodels no agrega el intercepto (b0) por defecto.
# Si no haces esto, la regresión forzará que la línea pase por cero (0,0).
X_con_constante = sm.add_constant(X)

# 4. CORRER EL MODELO MCO (OLS en inglés)
# OLS = Ordinary Least Squares (Mínimos Cuadrados Ordinarios)
modelo = sm.OLS(Y, X_con_constante)
resultados = modelo.fit()

# 5. IMPRIMIR EL REPORTE
print(resultados.summary())
