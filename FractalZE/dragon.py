# -*- coding: utf-8 *-*

from fractal import Fractal

from PIL import Image, ImageDraw

import math


class Dragon(Fractal):
	
	def __init__(self, l = 1):
		""" 
		@param l: longitud del segmento inicial. Default 1
		@type l: float
		
		"""
		
		self.l = float(l)
				
		
	def lindenmayer(self, n):
		"""Devuelve el fractal del dragón expresado en L-System 
		@param n: numero de termino de la sucesion
		@type n: int
		@return: fractal del dragón expresada en L-System.
		@rtype: string
		
		Algoritmo en L-System.
			- variables: X Y
			- constantes: F + -
			- axioma: FX
			- reglas:
				1. X -> X+YF+
				2. Y -> -FX-Y
		
		Interpretacion.
			1. Una F significa dibujar
			2. Un - significa girar a la izquierda 90 grados
			2. Un + significa girar a la derecha 90 grados
		
		"""
		
		lindenmayer = 'FX'
		for i in range(n):
			aux = ""
			for l in lindenmayer: 
				if(l == 'X'):
					aux += 'X+YF'
				elif(l == 'Y'):
					aux += 'FX-Y'
				else:
					aux += l
			lindenmayer = aux
		return lindenmayer	

		
	def getWidth(self, n=0):		
		return self.l * 3
		
			
	def getHeight(self, n=0):
		return self.l * 3
		
		
	def _generateGeometry(self, n):	
		x1, y1, angle = (self.getWidth(n)/2, self.getHeight(n)/2, math.pi/2)
		segmentLength = self.l / math.sqrt(2 ** n)
		lindenmayer = self.lindenmayer(n)
		lines = []
		
		for l in lindenmayer:
			if(l == 'F'):
				x2 = x1 + segmentLength * math.cos(angle)
				y2 = y1 - segmentLength * math.sin(angle)
				lines.append([(int(x1), int(y1)), (int(x2), int(y2))])
				x1, y1 = x2, y2
			elif(l == '+'):
				angle += math.pi/2
			else:
				angle -= math.pi/2
		return lines
		
