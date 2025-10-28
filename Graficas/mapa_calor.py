import matplotlib.pyplot as plt
import numpy as np

# Datos
matriz = np.random.rand(10, 10)

# Crear el mapa de calor
plt.imshow(matriz, cmap='hot', interpolation='nearest')

# Agregar barra de color
plt.colorbar()

# Agregar título
plt.title('Mapa de Calor')

# Mostrar la gráfica
plt.show()
