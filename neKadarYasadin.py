from datetime import *
dogumGunu = datetime.strptime(input("Doğum Gününü Gir (GÜN.AY.YIL): "),"%d.%m.%Y")
yas = datetime.now() - dogumGunu

print("Sen {} saniye yaşadın.".format(yas.total_seconds()))
