# -*- coding: utf-8 *-*

from fractal import Fractal

from PIL import Image, ImageDraw

import math


class Sierpinsky(Fractal):
    """Fractal o Triangulo de Sierpinsky.
    Construccion:
        1. Se parte de un triangulo equilatero.
        2. Se divide cada lado en dos obteniendose 3 puntos.
        3. Al unir los 3 puntos, el triangulo queda dividido en 4 triangulos.
        4. Se descarta el del medio, es decir el que esta invertido.
        5. Se repite esto sucesivamente con cada triangulo.
    
    """
    
    def __init__(self, l = 1):
        """ 
        @param l: longitud del lado maximo(cuando n=0).default = 1.
        @type l: float
        
        """
        
        self.l = float(l)
        
        
    def countTriangles(self, n):
        """Devuelve la cantidad de triangulos del termino n. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: cantidad de triangulos.
        @rtype: int
        
        """
        
        return 3 ** n
        
        
    def triangleArea(self, n):
        """Devuelve el area ocupada por un solo triangulo del termino n. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: area ocupada por un triangulo.
        @rtype: float
        
        """
        
        return self.l ** 2 / 2 ** (n + 1)
        
        
    def totalArea(self, n):
        """Devuelve el area total. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: area total.
        @rtype: float
        
        """
        
        return self.countTriangles(n) * self.triangleArea(n)
        
        
    def trianglePerimeter(self, n):
        """Devuelve el perimetro de un triangulo del termino n. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: perimetro de un triangulo.
        @rtype: float
        
        """
        
        return 3 * self.l / 2 ** n
        
        
    def totalPerimeter(self, n):
        """Devuelve la suma de los perimetros de todos los triangulos del termino n. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: perimetro total.
        @rtype: float
        
        """
        
        return self.countTriangles(n) * self.trianglePerimeter(n)
        
        
    def triangleHeight(self, n):
        """Devuelve la altura de un triangulo del termino n. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: altura de un triangulo.
        @rtype: float
        
        """
        
        return 0.5 * (self.l / 2 ** n) * math.sqrt(3)
        
        
    def triangleWidth(self, n):
        """Devuelve el ancho de un triangulo del termino n. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: ancho de un triangulo.
        @rtype: float
        
        """
        
        return self.l / 2 ** n

        
    def getWidth(self, n=0):
        """Devuelve el ancho del fractal. Siempre es igual a l
        @return: ancho del fractal
        @rtype: float
        
        """
        
        return self.triangleWidth(0)
        
            
    def getHeight(self, n=0):
        """Devuelve la altura del fractal.
        @return: ancho del fractal
        @rtype: float
        
        """
        
        return self.triangleHeight(0)
        
        
    def _generateGeometry(self, n):
        
        triangles = [self._initialTriangle()]
                                
        for i in range(n):
            aux = []
            for t in triangles:
                aux+= self._splitTriangle(t)
            triangles = aux
            
        return triangles

    
    def _splitTriangle(self, triangle):
        
        x1, y1 = triangle[0]
        x2, y2 = triangle[1]
        x3, y3 = triangle[2]
        
        x11 = x1
        y11 = y1
        x12 = 0.5 * (x1 - x2) + x2
        y12 = 0.5 * (y2 - y1) + y1
        x13 = 0.5 * (x3 - x1) + x1
        y13 = y12
        t1 = [(x11, y11), (x12, y12), (x13, y13)]
        t2 = [(x12, y12), (x2, y2), (x1, y2)]
        t3 = [(x13, y13), (x1, y2), (x3, y3)]
        return [t1, t2, t3]


    def _initialTriangle(self):
        
        x1 = self.l/2.0
        y1 = 0.0
        x2 = 0.0
        y2 = self.triangleHeight(0)
        x3 = self.l - 1
        y3 = y2
        return [(x1, y1), (x2, y2), (x3, y3)]
