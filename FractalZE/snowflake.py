# -*- coding: utf-8 *-*

from koch import Koch

from PIL import Image, ImageDraw

import math


class Snowflake(Koch):
    """Fractal de la bola de nieve.
    Cosntruccion:
        1. Se parte de un triangulo equilátero.
        2. Se divide cada segmento en 3 partes iguales.
        3. Se construye un triangulo equilatero sobre cada mitad de cada segmento.
        4. Se descartan los segmentos centrales(la base de los triangulo creados).
        5. Se repiten los pasos para cada segmento las veces que se quiera.
        
    
    """
    
    
    def countSegments(self, n):
        """Devuelve la cantidad de segmentos del termino n. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: cantidad de segmentos.
        @rtype: int
        
        """
        
        return 3 * 4**n
        
        
    def totalArea(self, n):
        """Devuelve el area total debajo de la curva. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: area total debajo de la curva.
        @rtype: float
        
        """
        
        if (n == 0):
            return self.l ** 2 / 2
        else:
            newTriangles = self.countSegments(n-1)
            minTriangleArea = self.segmentLength(n) ** 2 / 2
            return newTriangles * minTriangleArea + self.totalArea(n - 1)
            
        
    def getWidth(self, n=0):
        """Devuelve el ancho del fractal.
        @return: ancho del fractal
        @rtype: float
        
        """
        
        return self.l
        
            
    def getHeight(self, n=0):
        """Devuelve la altura del fractal.
        @return: altura del fractal
        @rtype: float
        
        """
        if (n == 0):
            return math.sqrt(3) * self.l / 2.0
        else:
            return 2.0 * math.sqrt(3) * self.l / 3.0
    
    def _getAxiomaLindenmayer(self):
        return '_-_-_'
    
    def _getInitialGeometry(self, n):
        return ((0.0, int(self.getHeight(0))), math.pi / 3)
