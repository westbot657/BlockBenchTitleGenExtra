# pylint: disable=W,R,C
from PIL import Image

class Shape:
    
    class Manager:
        def __init__(self, shapes):
            self.shapes = shapes
        
        def get(self, shape_id):
            for s in self.shapes:
                s: Shape
                if s.shape_id == shape_id:
                    return s
            return None
    
    def __init__(self, shape_id, color_key_grid):
        self.shape_id = shape_id
        self.color_key_grid = color_key_grid


    @classmethod
    def loadTileMap(cls, file_name:str) -> Manager:
        img = Image.open(file_name)
        
        pixel_data = list(img.getdata())
        width = img.width
        
        shapes = []
        
        def getChunk(x, y):
            out: list[list[tuple[int, int, int]]] = []
            for ry in range(y*4, (y+1)*4):
                out.append([])
                for rx in range(x*4, (x+1)*4):
                    out[-1].append(pixel_data[(ry * width) + rx])
            return out
        
        # Single pixel
        shapes.append(cls("FFFFFFFF", getChunk(0, 0)))
        
        # 3x3
        shapes.append(cls("FFFFTTTF", getChunk(2, 0)))
        shapes.append(cls("TFFFTTTT", getChunk(3, 0)))
        shapes.append(cls("TFFFFFTT", getChunk(4, 0)))
        shapes.append(cls("FFTTTTTF", getChunk(2, 1)))
        shapes.append(cls("TTTTTTTT", getChunk(3, 1)))
        shapes.append(cls("TTTFFFTT", getChunk(4, 1)))
        shapes.append(cls("FFTTTFFF", getChunk(2, 2)))
        shapes.append(cls("TTTTTFFF", getChunk(3, 2)))
        shapes.append(cls("TTTFFFFF", getChunk(4, 2)))
        
        # 1x3
        shapes.append(cls("FFFFFFTF", getChunk(0, 2)))
        shapes.append(cls("FFTFFFTF", getChunk(0, 3)))
        shapes.append(cls("FFTFFFFF", getChunk(0, 4)))
        
        # 3x1
        shapes.append(cls("FFFFTFFF", getChunk(2, 4)))
        shapes.append(cls("TFFFTFFF", getChunk(3, 4)))
        shapes.append(cls("TFFFFFFF", getChunk(4, 4)))
        
        # 3x3 hollow
        shapes.append(cls("FFFFTFTF", getChunk(0, 6)))
        #shapes.append(cls("TFFFTFFF", getChunk(1, 6)))
        shapes.append(cls("TFFFFFTF", getChunk(2, 6)))
        #shapes.append(cls("FFTFFFTF", getChunk(0, 7)))
        #shapes.append(cls("FFTFFFTF", getChunk(2, 7)))
        shapes.append(cls("FFTFTFFF", getChunk(0, 8)))
        #shapes.append(cls("TFFFTFFF", getChunk(1, 8)))
        shapes.append(cls("TFTFFFFF", getChunk(2, 8)))
        
        
        # star shape
        shapes.append(cls("FFFFFTTT", getChunk(4, 9)))
        
        shapes.append(cls("FFFTTTTT", getChunk(3, 10)))
        shapes.append(cls("TFTFTTTT", getChunk(4, 10)))
        shapes.append(cls("TTFFFTTT", getChunk(5, 10)))
        
        shapes.append(cls("FFFTTTTT", getChunk(2, 11)))
        shapes.append(cls("TFTTTFTT", getChunk(3, 11)))
        shapes.append(cls("TTTTTTFT", getChunk(4, 11)))
        shapes.append(cls("TTTFTTTF", getChunk(5, 11)))
        shapes.append(cls("TTFFFTTT", getChunk(6, 11)))
        
        shapes.append(cls("FFFTTTFF", getChunk(1, 12)))
        shapes.append(cls("TFTTTTTF", getChunk(2, 12)))
        shapes.append(cls("TTTTFTTT", getChunk(3, 12)))
        
        shapes.append(cls("FTTTTTTT", getChunk(5, 12)))
        shapes.append(cls("TTTFTFTT", getChunk(6, 12)))
        shapes.append(cls("TTFFFFFT", getChunk(7, 12)))
        
        shapes.append(cls("FTTTTTFF", getChunk(2, 13)))
        shapes.append(cls("TTTFTTTF", getChunk(3, 13)))
        shapes.append(cls("TTFTTTTT", getChunk(4, 13)))
        shapes.append(cls("TFTTTFTT", getChunk(5, 13)))
        shapes.append(cls("TTTTFFFT", getChunk(6, 13)))
        
        shapes.append(cls("FTTTTTFF", getChunk(3, 14)))
        shapes.append(cls("TTTTTFTF", getChunk(4, 14)))
        shapes.append(cls("TTTTFFFT", getChunk(5, 14)))
        
        shapes.append(cls("FTTTFFFF", getChunk(4, 15)))
        
        
        # idk what to call it
        shapes.append(cls("FFFFFFTT", getChunk(8,  0)))
        
        shapes.append(cls("FFFFFTTF", getChunk(12, 0)))
        
        
        
        shapes.append(cls("FFFTTTTT", getChunk(7,  1)))
        shapes.append(cls("TFTFFFTT", getChunk(8,  1)))
        
        shapes.append(cls("FFTFTTTF", getChunk(12, 1)))
        shapes.append(cls("TTFFFTTT", getChunk(13, 1)))
        
        
        
        shapes.append(cls("FFFTTTTT", getChunk(6,  2)))
        shapes.append(cls("TFTTTTTT", getChunk(7,  2)))
        shapes.append(cls("TTTFFTTT", getChunk(8,  2)))
        
        shapes.append(cls("FFTTTTTT", getChunk(12, 2)))
        shapes.append(cls("TTTFTTTT", getChunk(13, 2)))
        shapes.append(cls("TTFFFTTT", getChunk(14, 2)))
        
        
        
        shapes.append(cls("FFFTTFFF", getChunk(5,  3))) #
        shapes.append(cls("TFTTTFFF", getChunk(6,  3))) #
        shapes.append(cls("TTTTTTFF", getChunk(7,  3))) #
        shapes.append(cls("TTTFTFTF", getChunk(8,  3))) #
        shapes.append(cls("TTFFTTFT", getChunk(9,  3)))   #
        shapes.append(cls("TFFFTFTF", getChunk(10, 3)))   #
        shapes.append(cls("TFFTTTFT", getChunk(11, 3)))   #
        shapes.append(cls("TFTTTFTF", getChunk(12, 3))) #
        shapes.append(cls("TTTTTFFT", getChunk(13, 3))) #
        shapes.append(cls("TTTFTFFF", getChunk(14, 3))) #
        shapes.append(cls("TTFFFFFF", getChunk(15, 3))) #
        
        
        
        shapes.append(cls("FTTTFTTF", getChunk(8,  4)))
        
        shapes.append(cls("FTTTFTTT", getChunk(10, 4)))
        
        shapes.append(cls("FTTTFFTT", getChunk(12, 4)))
        
        
        
        shapes.append(cls("FFTFTFTF", getChunk(8,  5)))
        shapes.append(cls("TTFTTTFT", getChunk(9,  5)))
        shapes.append(cls("TFTFTFTF", getChunk(10, 5)))
        shapes.append(cls("TTFTTTFT", getChunk(11, 5)))
        shapes.append(cls("TFTFFFTF", getChunk(12, 5)))
        
        
        
        shapes.append(cls("FFTTFTTT", getChunk(8,  6)))
        
        shapes.append(cls("FTTTFTTT", getChunk(10, 6)))
        
        shapes.append(cls("FTTFFTTT", getChunk(12, 6)))
        
        
        
        shapes.append(cls("FFFFTTFF", getChunk(5,  7))) #
        shapes.append(cls("TFFFTTTF", getChunk(6,  7))) #
        shapes.append(cls("TFFTTTTT", getChunk(7,  7))) #
        shapes.append(cls("TFTFTFTT", getChunk(8,  7))) #
        shapes.append(cls("TTFTTFFT", getChunk(9,  7)))   #
        shapes.append(cls("TFTFTFFF", getChunk(10, 7)))   #
        shapes.append(cls("TTFTTTFF", getChunk(11, 7)))   #
        shapes.append(cls("TFTFTTTF", getChunk(12, 7))) #
        shapes.append(cls("TTFFTTTT", getChunk(13, 7))) #
        shapes.append(cls("TFFFTFTT", getChunk(14, 7))) #
        shapes.append(cls("TFFFFFFT", getChunk(15, 7))) #
        
        
        
        shapes.append(cls("FTTTTTFF", getChunk(6,  8)))
        shapes.append(cls("TTTTTTTF", getChunk(7,  8)))
        shapes.append(cls("TTTTFFTT", getChunk(8,  8)))
        
        shapes.append(cls("FTTTTTTF", getChunk(12, 8)))
        shapes.append(cls("TTTTTFTT", getChunk(13, 8)))
        shapes.append(cls("TTTTFFFT", getChunk(14, 8)))
        
        
        
        shapes.append(cls("FTTTTTFF", getChunk(7,  9)))
        shapes.append(cls("TTTFFFTF", getChunk(8,  9)))
        
        shapes.append(cls("FFTTTFTF", getChunk(12, 9)))
        shapes.append(cls("TTTTFFFT", getChunk(13, 9)))
        
        
        
        shapes.append(cls("FTTFFFFF", getChunk(8, 10)))
        
        shapes.append(cls("FFTTFFFF", getChunk(12,10)))
        
        
        return cls.Manager(shapes)
        
        














