import pandas as pd
from pandas.tseries.offsets import MonthEnd

# Definir la fecha de inicio y la fecha de corte para el último mes
start_date = pd.Timestamp("2015-01-01")
final_month_limit = pd.Timestamp("2025-02-18")

# Generar la lista de inicios de mes desde enero 2015 hasta febrero 2025
months = pd.date_range(start=start_date, end="2025-02-01", freq='MS')

ultimo_dia_habil = []

for month_start in months:
    # Si es el mes final (febrero 2025), considerar solo hasta el 18 de febrero
    if month_start.year == 2025 and month_start.month == 2:
        # Generar rango desde el 1 de febrero hasta el 18 de febrero de 2025
        dias_disponibles = pd.date_range(start=month_start, end=final_month_limit, freq='D')
        # Filtrar solo los días hábiles (lunes=0 a viernes=4)
        dias_habiles = [d for d in dias_disponibles if d.weekday() < 5]
        # El último día hábil disponible será el máximo de la lista
        ultimo = max(dias_habiles)
    else:
        # Para meses completos, obtener el último día del mes
        full_end = month_start + MonthEnd(0)
        # Si el último día es sábado (5) o domingo (6), ajustar al viernes
        if full_end.weekday() == 5:  # sábado
            ultimo = full_end - pd.Timedelta(days=1)
        elif full_end.weekday() == 6:  # domingo
            ultimo = full_end - pd.Timedelta(days=2)
        else:
            ultimo = full_end
    # Agregar a la lista formateando la fecha en dd-mm-yyyy
    ultimo_dia_habil.append(ultimo.strftime('%d-%m-%Y'))

# Crear el DataFrame con la columna correspondiente
df = pd.DataFrame(ultimo_dia_habil, columns=['Ultimo Dia Habil'])

# Guardar en un archivo CSV
csv_file_path = '/mnt/data/ultimo_dia_habil.csv'
df.to_csv(csv_file_path, index=False)

print(f"Archivo CSV generado: {csv_file_path}")
