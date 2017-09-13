import numpy as np
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]

def f(t): return 2.5*np.cos(2*np.pi*t)+2015

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.1)

plt.figure(1)
plt.subplot(211)
plt.plot(x, y, 'k--', t1, f(t1))
plt.title('David Sorcia Hernandez', fontsize = 20, color = 'green')
plt.xlabel('Edad', fontsize = 12, color = 'blue')
plt.ylabel('Anio', fontsize = 12, color = 'red')

plt.subplot(212)
plt.plot(t2, 2.5*np.cos(2*np.pi*t2)+2015,'y--')
plt.savefig('Pregunta3.png')
plt.show()

