# -*- coding: utf-8 *-*

from fractal import Fractal

from PIL import Image, ImageDraw

import math


class Arbol(Fractal):
	"""Fractal del arbol.
	Construccion:
		1. Se parte de un segmento.
		2. Desde la punta de cada rama se dibujan dos nuevos segmentos de la mitad de la longitud de la rama.
			1. El primero apuntando 60 grados a la izquierda de la direccion de la rama.
			2. El segundo apuntando 60 grados a la derecha de la direccion de la rama.
		3. Se repite esto sucesivamente con cada rama las veces que se desee.
	
	"""
	
	def __init__(self, l = 1, angle = math.pi / 6):
		""" 
		@param l: longitud del segmento maximo.
		@type l: float
		@param angle: angulo ramas en radianes
		@type angle: float
		
		"""
		
		self.l = float(l)
		self.angle = angle
	
	
	def segmentLength(self, n=0):
		"""Devuelve la longitud de un segmento del termino n. 
		@param n: numero de termino de la sucesion
		@type n: int
		@return: longitud de un segmento.
		@rtype: float
		
		"""
		
		return self.l/2**n
	
	
	def countSegments(self, n):
		"""Devuelve la cantidad de segmentos nuevos. 
		@param n: numero de termino de la sucesion
		@type n: int
		@return: cantidad de segmentos.
		@rtype: int
		
		"""
		
		return 2**n
	
	
	def totalLength(self, n):
		"""Devuelve la suma de la longitud de todos los segmentos. 
		@param n: numero de termino de la sucesion
		@type n: int
		@return: longitud total.
		@rtype: float
		
		"""
		
		if(n == 0):
			return self.l
		else:
			return self.segmentLength(n) * self.countSegments(n) + self.totalLength(n - 1)

			
		
	def lindenmayer(self, n):
		"""Devuelve el fractal del arbol expresado en L-System 
		@param n: numero de termino de la sucesion
		@type n: int
		@return: fractal expresado en L-System.
		@rtype: string
		
		Algoritmo en L-System.
			- variables: 0 1
			- constantes: [ ]
			- axioma: 0
			- reglas:
				1. 1 -> 11
				2. 0 -> 1[0]0
		
		Interpretacion.
			1. Un 0 significa dibujar una hoja (segmento de longitud L/2)
			2. Un 1 significa dibujar una rama (segmento de longitud L)
			3. Un [ significa guardar posicion y angulo en la pila, y girar X grados en sentido antihorario
			4. Un ] significa extraer posicion y angulo de la pila, y girar X grados en sentido horario
		
		"""
		
		lindenmayer = '0'
		for i in range(n):
			aux = ""
			for j in lindenmayer: 
				if(j == '0'):
					aux += '1[0]0'
				elif(j == '1'):
					aux += '11'
				else:
					aux += j
			lindenmayer = aux
		return lindenmayer		


	def getHeight(self, n, angle = math.pi / 2):
		"""Devuelve la altura del arbol. 
		@param n: numero de termino de la sucesion
		@type n: int
		@param angle: no se usa, necesario para la recursion
		@type angle: float
		@return: altura del arbol.
		@rtype: float
		
		"""
		if (n==0):
			return self.segmentLength(0)
			
		toLeft = abs(angle + self.angle)
		toRight = abs(angle - self.angle) 
		
		if (math.sin(toLeft) > math.sin(toRight)):
			angle = toLeft
		else:
			angle = toRight
			
		return math.sin(angle) * self.segmentLength(n) + self.getHeight(n-1, angle)
			
	
	def getWidth(self, n=0, angle = math.pi / 2):
		"""Devuelve el ancho del arbol. 
		@param n: numero de termino de la sucesion
		@type n: int
		@param angle: no se usa, necesario para la recursion
		@type angle: float
		@return: ancho del arbol.
		@rtype: float
		
		"""
		
		if(n==0):
			return 1.0
		else:
			toLeft = abs(angle + self.angle)
			toRight = abs(angle - self.angle) 
			if (math.cos(toLeft) > math.cos(toRight)):
				angle = toLeft
			else:
				angle = toRight
			return math.cos(angle) * self.segmentLength(n) * 2 + self.getWidth(n-1, angle)
		
	
	def _getInitialGeometry(self, n):
		x1 = (self.getWidth(n) / 2.0) - 1
		y1 = self.getHeight(n) 
		x2, y2 = (0.0, 0.0)
		angle = math.pi / 2.0
		leafLength = self.segmentLength(n)
		branchLength = leafLength * 2.0
		return (x1, y1, x2, y2, angle, branchLength, leafLength)
		
		
	def _generateGeometry(self, n):
		
		x1, y1, x2, y2, angle, branchLength, leafLength = self._getInitialGeometry(n)
		lindenmayer = self.lindenmayer(n)
		lifo = []
		lines = []
		
		for l in lindenmayer:
			if(l == '1'):
				x2 = x1 + branchLength * math.cos(angle)
				y2 = y1 - branchLength * math.sin(angle)
				lines.append([(int(x1), int(y1)), (int(x2), int(y2))])
				x1, y1 = x2, y2
			elif(l == '0'):
				x2 = x1 + leafLength * math.cos(angle)
				y2 = y1 - leafLength * math.sin(angle)
				lines.append([(int(x1), int(y1)), (int(x2), int(y2))])
				x1, y1 = x2, y2
			elif(l == '['):
				lifo.append((x1, y1, angle))
				angle += self.angle
			else:
				x1, y1, angle = lifo.pop()
				angle -= self.angle
		
		return lines
