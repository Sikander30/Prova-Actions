import os
from pyhtml2pdf import converter

path = path = os.path.abspath('html/prova.html')
print(f'File to convert: {path}')
converter.convert(f'file:///{path}', '../pdf/prova.pdf')
