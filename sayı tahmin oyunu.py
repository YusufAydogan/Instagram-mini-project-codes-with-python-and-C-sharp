from random import randint
rand = randint(1, 60)
sayac = 0
 
while True:
    sayac += 1
    sayi = int(input("1 ile 60 arasında değer girin (çıkış için 0):"))
    if(sayi == 0):
        print("Oyunu İptal Edildi...")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı:",rand )
        print("Tahmin sayınız:",sayac)
        
        
       # @mr.code_engineer instagram hesabını takip etmeyi unutmayın :)
