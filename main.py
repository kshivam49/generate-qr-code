#pip install qrcode
import qrcode

data='Shivam kumar'

img=qrcode.make(data)

img.save('E:/my code/my python projects/qr code/myqrcode.png')