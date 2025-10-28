import matplotlib.pyplot as plt
import numpy as np

# Datos
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Crear el diagrama de caja
plt.boxplot(data, labels=['Desv=1', 'Desv=2', 'Desv=3'])

# Agregar título
plt.title('Diagrama de Caja')

# Mostrar la gráfica
plt.show()
