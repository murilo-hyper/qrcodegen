import pyqrcode


link = ''
pyqrcode.create(link).svg('qrcode.svg', scale=10)