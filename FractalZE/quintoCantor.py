# -*- coding: utf-8 *-*

from PIL import Image, ImageDraw

import math

from cantor import Cantor

		
class QuintoCantor(Cantor):
	"""Fractal de cantor que divide los segmentos en 5 y descarta el del medio.
	
	"""
		
	
	def segmentLength(self, n):
		"""Devuelve la longitud de un segmento del termino n. 
		@param n: numero de termino de la sucesion
		@type n: int
		@return: longitud de un segmento.
		@rtype: float
		
		"""
		
		return self.l * ((2.0 / 5.0) ** n)
		
		
	def lindenmayer(self):
		pass
