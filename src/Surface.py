# pylint: disable=W,R,C
from PIL import Image

# Colors:
# top side: #b0b0b0
# face: #ffffff
# bottom side: #545454

class Surface:
    def __init__(self, input_file, output_file):
        self.img = Image.open(input_file)
        self.of = output_file
        self.pixel_nodes = []
        self.shape_nodes = []

        self.shapes = []

