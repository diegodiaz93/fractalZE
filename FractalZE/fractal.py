# -*- coding: utf-8 *-*
    
from PIL import Image, ImageDraw

import math

class Fractal:
        
        
    def graph(self, n=0, mode = '1', fillColor='black', lineColor = 'white', backgroundColor='white'):
        """Grafica el fractal. 
        @param n: numero de termino de la sucesion
        @type n: int 
        @param mode: modo imagen(RGB, 1, etc)
        @type mode: string
        @param fillColor: color de relleno
        @type fillColor: RGB or string
        @param lineColor: color de linea
        @type lineColor: RGB or string
        @param backgroundColor: color de fondo
        @type backgroundColor: RGB or string  
        @return: imagen del fractal. 
        @rtype: Image
                
        """
        
        width = int(self.getWidth(n))
        height = int(self.getHeight(n))
        image = Image.new(mode, (width, height), backgroundColor)
        geometry = self._generateGeometry(n)
        self._drawGeometry(image, geometry, fillColor, lineColor)
        return image
    
    def _drawGeometry(self, image, geometry, fillColor='black', lineColor = 'white'):
        draw = ImageDraw.Draw(image)
        for g in geometry:
            if (len(g) == 2):
                draw.line(g, fill = lineColor)
            else:
                draw.polygon(g, fill = fillColor, outline = lineColor)
