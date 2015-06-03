# -*- coding: utf-8 *-*

from PIL import Image, ImageDraw

import math

from sierpinsky import Sierpinsky


class SierpinskyRectangular(Sierpinsky):
	"""Sierpisnky rectangulo isosceles.
	
	"""	
		
	def trianglePerimeter(self, n):
		"""Devuelve el perimetro de un triangulo del termino n. 
		@param n: numero de termino de la sucesion
		@type n: int
		@return: perimetro de un triangulo.
		@rtype: float
		
		"""
		
		return self.l * (2 + math.sqrt(2)) / 2 ** n
		
		
	def triangleHeight(self, n):
		"""Devuelve la altura de un triangulo del termino n. 
		@param n: numero de termino de la sucesion
		@type n: int
		@return: altura de un triangulo.
		@rtype: float
		
		"""
		
		return self.l / 2 ** n

	
	def _splitTriangle(self, triangle):
		
		x1, y1 = triangle[0]
		x2, y2 = triangle[1]
		x3, y3 = triangle[2]
			
		x11 = x1
		y11 = y1
		x12 = x1
		y12 = 0.5 * (y2 - y1) + y1
		x13 = 0.5 * (x3 - x1) + x1
		y13 = y12
		t1 = [(x11, y11), (x12, y12), (x13, y13)]
		t2 = [(x1, y12), (x2, y2), (x13, y2)]
		t3 = [(x13, y13), (x13, y2), (x3, y3)]
		return [t1, t2, t3]


	def _initialTriangle(self):
		
		x1 = 0.0
		y1 = 0.0
		x2 = 0.0
		y2 = self.l - 1
		x3 = self.l - 1
		y3 = y2
		return [(x1, y1), (x2, y2), (x3, y3)]
