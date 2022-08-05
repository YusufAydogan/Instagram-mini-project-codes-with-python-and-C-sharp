import string
import random

while True: 
#Döngü oluşturduk çünkü her seferinde programı tekrar çalıştırmaya gerek yok.

    print("----------------------------------")
    print("Parola Oluşturucuya Hoşgeldiniz...")

    uzunluk = int(input("Parolanızın uzunluğunu belirleyiniz: "))

    icerik = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    # Burada hem küçük hem büyük harf, hem sayılar hem de sembollerin olacağını belirtiyoruz.

    karistir = random.sample(icerik,uzunluk)
    #Burada içeriği ve uzunluğu kullanarak bir şifre oluşturmasını söylüyoruz.

    sifreniz = "".join(karistir)
    #Oluşturulan şifreyi "sifreniz" değişkenine atadık.

    print(sifreniz)
    #Ve hazırlanan şifreyi kullanıcıya sıcak sıcak servis ediyoruz, afiyet olsun :)
    
