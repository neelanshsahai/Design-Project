from PIL import Image
import os


class Conversions:
    def __init__(self, name):
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.orig_name = name;
        self.bnw_name = "black-n-white_" + name

    def colored_to_grayscale(self):
        os.chdir(self.path+'/../Images')
        if not os.path.exists('Black-n-White Images'):
            os.mkdir('Black-n-White Images')
        os.chdir('Black-n-White Images')

        Image.open('../Original Images/'+self.orig_name).convert('L').save(self.bnw_name)
