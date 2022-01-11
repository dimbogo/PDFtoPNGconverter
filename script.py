from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from PIL import Image
import os
import tempfile

files = os.listdir()
with tempfile.TemporaryDirectory() as path:
    images = convert_from_path(f'{os.getcwd()}\{files[0]}', output_folder=path)
    for counter, image in enumerate(images):
        name = str(counter + 1)
        image.save(f"{name}.png", 'png')



