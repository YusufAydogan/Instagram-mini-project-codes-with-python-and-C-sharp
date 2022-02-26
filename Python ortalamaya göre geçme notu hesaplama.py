vize1 = int(input("1.Vize notunuzu giriniz: "))
vize2 = float(input("2.Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))

ort = (vize1*0.3) + (vize2*0.3) + (final*0.4)

if ort>=90:
    print("'AA'  ==>",ort)
elif ort>=85 and ort<90:
    print("'BA'  ==>",ort)
elif ort>=80 and ort<85:
    print("'BB'  ==>",ort)
elif ort>=75 and ort<80:
    print("'CB'  ==>",ort)
elif ort>=70 and ort<75:
    print("'CC'  ==>",ort)
elif ort>=65 and ort<70:
    print("'DC'  ==>",ort)
elif ort>=60 and ort<65:
    print("'DD'  ==>",ort)
elif ort>=50 and ort<60:
    print("'FD'  ==>",ort)
elif ort<50:
    print("'FF'  ==>",ort)
