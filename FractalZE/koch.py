# -*- coding: utf-8 *-*

from fractal import Fractal

from PIL import Image, ImageDraw

import math


class Koch(Fractal):
    """Fractal de la curva de Koch.
    Cosntruccion:
        1. Se parte de un segmento.
        2. Se divide el segmento en 3 partes iguales.
        3. Se construye un triangulo equilatero sobre el segmento central.
        4. Se descarta el segmento central(la base del triangulo).
        5. Se repiten los pasos para cada segmento las veces que se quiera.
        
    
    """
    
    def __init__(self, l = 1):
        """ 
        @param l: longitud del segmento maximo(cuando n=0). Default 1
        @type l: float
        
        """
        
        self.l = float(l)
    
    
    def segmentLength(self, n):
        """Devuelve la longitud de un segmento del termino n. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: longitud de un segmento.
        @rtype: float
        
        """
        
        return self.l/3**n
    
    
    def countSegments(self, n):
        """Devuelve la cantidad de segmentos del termino n. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: cantidad de segmentos.
        @rtype: int
        
        """
        
        return 4**n
    
    
    def totalLength(self, n):
        """Devuelve la suma de la longitud de todos los segmentos. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: longitud total.
        @rtype: float
        
        """
        
        return self.countSegments(n) * self.segmentLength(n)
        
        
    def totalArea(self, n):
        """Devuelve el area total debajo de la curva. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: area total debajo de la curva.
        @rtype: float
        
        """
        
        if (n == 0):
            return 0
        else:
            newTriangles = self.countSegments(n-1)
            minTriangleArea = self.segmentLength(n) ** 2 / 2
            return newTriangles * minTriangleArea + self.totalArea(n - 1)
            
        
    def lindenmayer(self, n):
        """Devuelve la curva de koch expresada en L-System 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: curva de koch expresada en L-System.
        @rtype: string
        
        Algoritmo en L-System.
            - variables: _
            - constantes: +-
            - axioma: _
            - reglas:
                1. _ -> _+_-_+_
        
        Interpretacion.
            1. Un _(guion bajo) significa dibujar un segmento
            2. Un +(mas) significa girar en sentido antihorario 60 grados
            2. Un -(menos) significa girar en sentido horario 120 grados
        
        """
        
        lindenmayer = self._getAxiomaLindenmayer()
        for i in range(n):
            aux = ""
            for l in lindenmayer: 
                if(l == '_'):
                    aux += '_+_-_+_'
                else:
                    aux += l
            lindenmayer = aux
        return lindenmayer  

        
    def getWidth(self, n=0):
        """Devuelve el ancho del fractal.
        @return: ancho del fractal
        @rtype: float
        
        """
        
        return self.l
        
            
    def getHeight(self, n):
        """Devuelve la altura del fractal.
        @return: altura del fractal
        @rtype: float
        
        """
        if (n == 0):
            return 1
        else:
            return self.l * math.sqrt(3) / 6
            
    
    def _getAxiomaLindenmayer(self):
        return '_'
        
        
    def _getInitialGeometry(self, n):
        return ((0.0, self.getHeight(n)-1.0), 0.0)
    
    
    def _generateGeometry(self, n): 
        point, angle = self._getInitialGeometry(n)
        lindenmayer = self.lindenmayer(n)
        segmentLength = self.segmentLength(n)
        polygon = [point]
        x1, y1 = point
        x2, y2 = (0.0, 0.0)
                
        for l in lindenmayer:
            if (l == '_'):
                x2 = x1 + segmentLength * math.cos(angle)
                y2 = y1 - segmentLength * math.sin(angle)
                x1 = x2
                y1 = y2
                polygon.append((x1,y1))
            elif (l == '+'):
                angle += math.pi / 3
            elif (l == '-'):
                angle -= 2 * math.pi / 3
        return [polygon]
        
