import numpy as np
import pylab as pl

x= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y= [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]

pl.title('David Sorcia Hernandez', fontsize = 20, color = 'green')
pl.xlabel('Edad', fontsize = 12, color = 'blue')
pl.ylabel('Anio', fontsize = 12, color = 'red')

pl.axis([0,20, 1997,2017])
pl.plot(x,y)

pl.savefig('Pregunta1.png')
