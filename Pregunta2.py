import numpy as np
import matplotlib.pyplot as plt

def f(t): return 2.5*np.cos(2*np.pi*t)+2015

t1 = np.arange(0.0, 5.0 ,0.1)

plt.plot(t1, f(t1), 'y--')
plt.savefig('Pregunta2.png')
plt.show()
