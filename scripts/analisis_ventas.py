import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('resultados', exist_ok=True)
df = pd.read_csv('datos/ventas.csv')
df['total_venta'] = df['cantidad'] * df['precio']

ventas_totales = df['total_venta'].sum()
producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()

df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.to_period('M')
ventas_por_mes = df.groupby('mes')['total_venta'].sum()

plt.figure(figsize=(10, 6))
ventas_por_mes.plot(kind='bar', color='coral', edgecolor='black')
plt.title('Evolución de Ventas por Mes')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales ($)')
plt.xticks(rotation=0)
plt.tight_layout()

ruta_grafico = 'resultados/evolucion_ventas.png'
plt.savefig(ruta_grafico)
