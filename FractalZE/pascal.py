# -*- coding: utf-8 *-*

from fractal import Fractal

from PIL import Image, ImageDraw, ImageFont

import math

        
class Pascal(Fractal):
    """Fractal del triángulo de Pascal.
        1. Cada fila tiene un boque mas que la anterior.
        2. La primer fila tiene un solo bloque que vale 1.
        3. Cada fila comienza y termina con un bloque que vale uno.
        4. Cada bloque contiene la suma de los valores de los dos bloques superiores.
        
    
    """
    
    def __init__(self, blockWidth=10.0, blockHeight = 10.0):
        """ 
        @param blockWidth: ancho del bloque.
        @type blockWidth: float
        @param blockHeight: alto del bloque
        @type blockHeight: float
        
        """
        self.blockWidth = blockWidth
        self.blockHeight = blockHeight
        self.fn = lambda x, y, n: 'yellow'
    
        
    def getWidth(self, n=0):
        """Devuelve el ancho del fractal.
        @return: ancho del fractal
        @rtype: float
        
        """
        
        return (n+1)*self.blockWidth
        
            
    def getHeight(self, n=0):
        """Devuelve la altura del fractal.
        @return: alto del fractal
        @rtype: float
        
        """
        
        return (n+1)*self.blockHeight
        
        
    def _generateBlocks(self, n=0):
        if(n==0):
            return [[1]]
        elif(n==1):
            return [[1], [1, 1]]
        else:
            blocks = [[1], [1, 1]]
            for i in range(n-1):
                lastBlock = blocks[-1]
                newBlock = [1]
                for j in range(len(lastBlock) - 1):
                    newBlock.append(lastBlock[j] + lastBlock[j+1])
                newBlock.append(1)
                blocks.append(newBlock)
            return blocks

    
    
    def _drawGeometry(self, image, geometry, fillColor='black', lineColor = 'white'):
        draw = ImageDraw.Draw(image)
        for g in geometry:
            p = g[0]
            x, y, n = g[1]
            fillColor = self.fn(x, y, n)
            draw.polygon(p, fill = fillColor, outline = lineColor)
            draw.text((p[0][0]+1, p[0][1]), str(n), fill='black')
        
        
    def _generateGeometry(self, n):
        lines = self._generateBlocks(n)
        geometry = []
        
        for l in range(len(lines)):
            blocks  = lines[l] 
            y1 = self.blockHeight * l
            y2 = y1 + self.blockHeight
            x0 = (self.getWidth(n) - len(blocks) * self.blockWidth) / 2.0
            for b in range(len(blocks)):
                block = blocks[b]
                x1 = x0 + self.blockWidth * b
                x2 = x1 + self.blockWidth
                p1 = (int(x1), int(y1))
                p2 = (int(x2), int(y1))
                p3 = (int(x2), int(y2))
                p4 = (int(x1), int(y2))
                geometry.append([[p1, p2, p3, p4], (b, l, block)])
                
        return geometry
        
