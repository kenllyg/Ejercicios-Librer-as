import matplotlib.pyplot as plt

# Preparamos los datos 
dias =['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
ventas =[120, 85, 150, 200, 170]

# Creamos el gráfico de barras
plt.bar(dias, ventas, color='yellow')

# Personalizamos el gráfico
plt.title('Ventas de la Semana')
plt.xlabel('Días de la Semana')
plt.ylabel('Cantidad de productos vendidos')

#Mostramos el resultado
plt.show()