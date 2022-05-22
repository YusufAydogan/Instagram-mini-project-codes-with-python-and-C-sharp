#Öncelikle kütüphanemizi indirelim.
#pip install qrcode
#sıra kodlarda

import qrcode

data = "istediğiniz metin, liste veya linki girebilirsiniz."

image = qrcode.make(data)

image.save("QRcode.png")


#gördüğünüz uzere istediğiniz uzantıyı kullanabilirsiniz.
#jpg, png vb.

#İşte bu kadar!
