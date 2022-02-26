boy = float(input("Boyunuzu giriniz: "))
kilo = float(input("Kilonuzu giriniz: "))
endeks = kilo/(boy**2)

if(endeks<=18.49):
    print("Boy - Kilo Endeksi Sonucu: ",endeks,"(ZAYIF)")
    
elif((18.49<endeks) and (endeks<25)):
    print("Boy - Kilo Endeksi Sonucu: ",endeks,"(İDEAL)")
    
elif(endeks>=25):
    print("Boy - Kilo Endeksi Sonucu: ",endeks,"(OBEZ)")
