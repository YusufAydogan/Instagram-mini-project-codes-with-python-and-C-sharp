#öncelikle terminale gelip kütüphaneyi kurun: "pip install qrcode"

import qrcode

qr = qrcode.QRCode(
    version=1, #1'den 40'a kadar versiyon kullanabilirsiniz.
    error_correction = qrcode.constants.ERROR_CORRECT_L, 
    box_size=10, #kutucuk boyutu
    border=2 #kenar boşluğu
    )

gidenDeger = "İstediğiniz metin veya linki girin."

qr.add_data(gidenDeger)
qr.make(fit=True)

resim = qr.make_image(fill_color="red", back_color="white") 
#Yukarıdaki satırda olduğu gibi istediğiniz ana ve arkaplan rengini kullanabilirsiniz.
resim.save("advenceQR.png") #Ve son olarak istediğiniz isimde kaydedebilirsiniz.
