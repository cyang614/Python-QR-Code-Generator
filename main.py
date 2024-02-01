import pyqrcode
from pyqrcode import QRCode

s = "https://www.youtube.com/watch?v=kS-fTMj7XDA"

url = pyqrcode.create(s)

url.svg("myyoutube.svg",scale = 8)