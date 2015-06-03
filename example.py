# -*- coding: utf-8 *-* 
import math
from FractalZE.cantor import Cantor
from FractalZE.sierpinsky import Sierpinsky
from FractalZE.sierpinskyRectangular import SierpinskyRectangular
from FractalZE.koch import Koch
from FractalZE.snowflake import Snowflake
from FractalZE.arbol import Arbol
from FractalZE.quintoCantor import QuintoCantor
from FractalZE.dragon import Dragon
from FractalZE.pascal import Pascal

print "Generando Cantor"
c = Cantor(600, 200)
for i in range(5):
	g = c.graph(i, mode='RGB', fillColor = 'red', lineColor='red')
	g.save('images/cantor%s.png' % i)

print "Generando Quinto Cantor"
c = QuintoCantor(600, 50)
for i in range(5):
	g = c.graph(i, mode='RGB', fillColor = (160, 70, 200), lineColor=(160, 70, 200))
	g.save('images/quintpocantor%s.png' % i)

print "Generando Koch"
k = Koch(600)
for i in range(8):
	g = k.graph(i, mode='RGB', fillColor = 'orange', lineColor = 'orange')
	g.save('images/koch%s.png' % i)

print "Generando Snowflake"
s = Snowflake(600)
for i in range(8):
	g = s.graph(i, mode='RGB', fillColor = (140, 230, 220), lineColor = 'blue')
	g.save('images/snowflake%s.png' % i)

print "Generando Sierpinsky"
s = Sierpinsky(600)
for i in range(8):
	g = s.graph(i, mode='RGB', fillColor = 'pink', lineColor = 'blue')
	g.save('images/sierpinsky%s.png' % i)

print "Generando Sierpinsky Rectangular"
s = SierpinskyRectangular(600)
for i in range(8):
	g = s.graph(i, mode='RGB', fillColor = 'red', lineColor = 'red')
	g.save('images/sierpinskyrectangular%s.png' % i)

print "Generando Árbol"
a = Arbol(600, math.pi/3)
for i in range(11):
	g = a.graph(i, mode='RGB', lineColor = 'blue')
	g.save('images/arbol%s.png' % i)

print "Generando Dragón"
d = Dragon(600)
for i in range(20):
	g = d.graph(i, mode='RGB', lineColor = 'black', fillColor='black')
	g.save('images/dragon%s.png' % i)

print "Generando Pascal"
p = Pascal(25)
p.fn = lambda x, y, n: 'white'	
g = p.graph(16, mode='RGB', lineColor='blue')
g.save('images/pascal.png')

print "Generando Pascal Pares"
pares = lambda x, y, n: 'white' if (n%2) == 0 else 'black'
p.fn = pares	
g = p.graph(16, mode='RGB', lineColor='blue')
g.save('images/pascalpares.png')

print "Generando Pascal Modulo 3"
modulo3 =  lambda x, y, n: 'yellow' if (n%3) == 0 else 'green'
p.fn = modulo3	
g = p.graph(16, mode='RGB', lineColor='blue')
g.save('images/pascalmodulo3.png')

print "Generando Pascal Triangulares"
triangulares = lambda x, y, n: 'red' if y == x+2 else 'yellow'
p.fn = triangulares	
g = p.graph(16, mode='RGB', lineColor='blue')
g.save('images/pascaltriangulares.png')

print "Generando Pascal Naturales"
naturales = lambda x, y, n: 'red' if x == 1 else 'yellow'
p.fn = naturales	
g = p.graph(16, mode='RGB', lineColor='blue')
g.save('images/pascalnaturales.png')

print "Generando Pascal Triangulares 2"
triangulares = lambda x, y, n: 'red' if x == 2 else 'yellow'
p.fn = triangulares	
g = p.graph(16, mode='RGB', lineColor='blue')
g.save('images/pascaltriangulares2.png')

print "Generando Pascal Tetraédricos 3d"
tetraedricos3d = lambda x, y, n: 'red' if x == 3 else 'yellow'
p.fn = tetraedricos3d
g = p.graph(16, mode='RGB', lineColor='blue')
g.save('images/pascaltetraedricos3d.png')

print "Generando Pascal Triangulares 4d"
triangulares4d = lambda x, y, n: 'red' if x == 4 else 'yellow'
p.fn = triangulares4d	
g = p.graph(16, mode='RGB', lineColor='blue')
g.save('images/pascaltriangulares4d.png')

print "Generando Pascal Triangulares 5d"
triangulares5d = lambda x, y, n: 'red' if x == 4 else 'yellow'
p.fn = triangulares5d	
g = p.graph(16, mode='RGB', lineColor='blue')
g.save('images/pascaltriangulares5d.png')

print "Generando Pascal Cuadrados"
def cuadrados(x, y, n):
	if (y == x+2):
		if(y % 2 == 0):
			return 'yellow'
		else:
			return 'red'
	return 'white'
p.fn = cuadrados	
g = p.graph(16, mode='RGB', lineColor='blue')
g.save('images/pascalcuadrados.png')
