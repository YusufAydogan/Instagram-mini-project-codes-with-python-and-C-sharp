bakiye = 1000;

while True:
    print("----------------------------------")
    print("mr.code_engineer ATM'ye Hoşgeldiniz...")
    print("----------------------------------")

    print("Bakiye görüntülemek istiyorsanız lütfen '1'e basınız.")
    print("Hesabınıza para çekmek istiyorsanız lütfen '2'e basınız.")
    print("Hesabınızdan para yatırmak istiyorsanız lütfen '3'e basınız.")
    print("ATM'den çıkmak istiyorsanız lütfen '4'e basınız.")
    islem = input("Yapmak istediğiniz işlemi seçiniz: ")
    

    if islem == "1":
        print("Bakiyeniz: ", bakiye)
        
    elif islem == "2":
        miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
        if miktar > bakiye:
            print("Bakiyeniz yetersizdir.")
        else:
            bakiye -= miktar
            print("Çekme işlemi başarılı.")
            print("Bakiyeniz: ",bakiye)

    elif islem == "3":
        miktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
        bakiye += miktar
        print("Yatırma işlemi başarılı.")
        print("Bakiyeniz: ",bakiye)

    elif islem == "4":
        print("ATM'den çıkış yapılıyor...")
        break
    
    
