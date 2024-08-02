#install the qrcode module using pip install qrcode 

#importing the module
import qrcode as qr

# creating variable
img = qr.make("https://www.youtube.com/")
img.save("youtube_home.png")