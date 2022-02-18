while True:
    tur = int(input("oluşturmak istediğiniz şeklin kenar sayısını giriniz: "))

    if(tur==3):
        a= int(input("a: "))
        b= int(input("b: "))
        c= int(input("c: "))

        if(a+b>c and a+c>b and b+c>a):
            if(a==b and b==c and a==c):
                print("Eşkenar üçgendir...")
            
            elif((a==b and a!=c) or (a==c and a!=b)):
                print("İkizkenar üçgendir...")

            elif(a!=b and a!=c and b!=c):
                print("Çeşitkenar üçgendir...")
            
        else:
            print("Üçgen oluşturulmaz...")
            
    elif(tur==4):
        a= int(input("a: "))
        b= int(input("b: "))
        c= int(input("c: "))
        d= int(input("d: "))

        if(a==b and b==c and a==c and a==d):
            print("Karedir...")

        elif((a==b and c==d) or (a==c and b==d) or (b==c and a==d)):
            print("Dikdörtgendir...")
        else:
            print("dörtgen oluşturulmaz...")
    
    else:
        print("Geçersiz şekil...")

    
