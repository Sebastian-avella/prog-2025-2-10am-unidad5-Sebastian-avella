import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Crear figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Datos
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Crear la superficie
ax.plot_surface(X, Y, Z, cmap='viridis')

# Agregar título
ax.set_title('Gráfica 3D de Superficie')

# Mostrar la gráfica
plt.show()
