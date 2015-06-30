# -*- coding: utf-8 *-*

from fractal import Fractal

from PIL import Image, ImageDraw

import math

        
class Cantor(Fractal):
    """Fractal de Cantor.
    Construccion:
        1. Se parte de un segmento.
        2. Se lo divide en 3 partes iguales.
        3. Se descarta la del medio.
        4. Se repite esto sucesivamente con cada segmento las veces que se desee.
    
    """
    
    def __init__(self, l=1.0, segmentHeight=1):
        """ 
        @param l: longitud del segmento maximo. Default 1
        @type l: float
        @param segmentHeight: altura que va a tener el segmento al dibujarlo(en pixels)
        @type segmentHeight: int
        
        """
        
        self.l = float(l)
        self.segmentHeight = segmentHeight
    
    
    def countSegments(self, n):
        """Devuelve la cantidad de segmentos  del termino n. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: cantidad de segmentos.
        @rtype: int
        
        """
        
        return 2 ** n
    
    
    def segmentLength(self, n):
        """Devuelve la longitud de un segmento del termino n. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: longitud de un segmento.
        @rtype: float
        
        """
        
        return self.l * 3 ** -n
    
    
    def totalLength(self, n):
        """Devuelve la suma de la longitud de todos los segmentos de un termino. 
        @param n: numero de termino de la sucesion
        @type n: int
        @return: longitud total.
        @rtype: float
        
        """
        
        return self.countSegments(n) * self.segmentLength(n)
        
        
    def lindenmayer(self, n=0):
        """Devuelve el fractal de cantor expresado en L-System.
        @param n: termino de la sucesion
        @type n: int 
        @return: termino expresado en L-system. 
        @rtype: string
        
        Algoritmo en L-System.
            - variables: _ (space)
            - constantes: 
            - axioma: _
            - reglas:
                1. _ -> _ _
                2. (space) -> (space)(space)(space)
        
        Interpretacion.
            1. Un _(guion bajo) significa dibujar un segmento
            2. Un (space) significa avanzar la longitud de un segmento sin dibujar
        
        """
        
        lindenmayer = '_'
        for i in range(n):
            newTerm = ''
            for l in lindenmayer: 
                if(l == '_'):
                    newTerm += '_ _'
                else:
                    newTerm += '   '
            lindenmayer = newTerm
        return lindenmayer
        
        
    def getWidth(self, n=0):
        """Devuelve el ancho del fractal.
        @return: ancho del fractal
        @rtype: float
        
        """
        
        return self.l
        
            
    def getHeight(self, n=0):
        """Devuelve la altura del fractal.
        @return: alto del fractal
        @rtype: float
        
        """
        
        return self.segmentHeight
        
        
    def _generateGeometry(self, n):
        lines = [(0.0, self.l-1)]
        for i in range(1, n+1):
            aux = []
            for l in lines:
                x1, x2 = l
                size = self.segmentLength(i)
                aux.append((x1, x1+size))
                aux.append((x2-size, x2))
            lines = aux
        
        polygons = []
        y2 = int(self.segmentHeight - 1)
        for l in lines:
            x1, x2 = l
            polygons.append([(int(x1), 0), (int(x2), 0), (int(x2), y2), (int(x1), y2)])
        
        return polygons
        
