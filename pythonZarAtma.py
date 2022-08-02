import random

def zarGorsel(zar):
    
    zar1 = """-----------------
|               |
|               |
|               |
|       o       |
|               |
|               |
|               |
-----------------"""

    zar2 = """-----------------
|o              |
|               |
|               |
|               |
|               |
|               |
|              o|
-----------------"""   
    
    zar3 = """-----------------
| o             |
|               |
|               |
|       o       |
|               |
|               |
|              o|
-----------------"""

    zar4 = """-----------------
|o             o|
|               |
|               |
|               |
|               |
|               |
|0             o|
-----------------"""

    zar5 = """-----------------
|o             o|
|               |
|               |
|       o       |
|               |
|               |
|o             o|
-----------------"""

    zar6 = """-----------------
|o             o|
|               |
|               |
|o             o|
|               |
|               |
|o             o|
-----------------"""


    if zar == 1:
        print(zar1)
    elif zar == 2:
        print(zar2)
    elif zar == 3:
        print(zar3)
    elif zar == 4:
        print(zar4)
    elif zar == 5:  
        print(zar5)
    elif zar == 6:
        print(zar6)


zar = random.randint(1,6)
print("Zarınız:" + str(zar))
zarGorsel(zar)
