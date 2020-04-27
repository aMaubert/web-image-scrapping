from PIL import  Image


class ImageEditor:

    def __init__(self, file_path):
        self.file_path = file_path

    def resize(self, size, convert_mode):
        image = Image.open(self.file_path)
        image = image.convert(convert_mode)
        image = image.resize(size)
        image.save(self.file_path)
