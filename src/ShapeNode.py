# pylint: disable=W,R,C

class ShapeNode:
    
    def __init__(self, x:int, y:int, color:tuple[int, int, int, int]):
        self.x = x
        self.y = y
        self.color = color
        self.left = False
        self.up_left = False
        self.up = False
        self.up_right = False
        self.right = False
        self.down_right = False
        self.down = False
        self.down_left = False

    def get_shape(self) -> str:
        return f"{str(self.left)[0]}{str(self.up_left)[0]}{str(self.up)[0]}{str(self.up_right)[0]}{str(self.right)[0]}{str(self.down_right)[0]}{str(self.down)[0]}{str(self.down_left)[0]}"
