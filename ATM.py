print("""*****************************
ATM Bankomat

1. Balansa baxmaq.

2. Pul yukleme.

3. Pul cixarma.

4. Karti qaytarmaq.
*****************************""")
hesab= 1000

while True:
    islem = input("Isleminiz:")
    
    if (islem == "1"):
        print("Balansiniz {} manatdir.".format(hesab))
        continue
    elif (islem == "2"):
        miqdar =int(input("Miqdar:"))
        print("Hesabiniz artirildi.")
        
        hesab += miqdar
    elif (islem == "3"):
        miqdar= int(input("Miqdar:"))     
        if (hesab-miqdar<0):
            print("Balansinizda kifayet qeder mebleg yoxdur.")
        else:
            print("Zehmet olmazsa,gozleyin...")
            hesab-=miqdar
    elif (islem == "e"):
        print("Kart geri qaytarilir...")
        break
    else:
        print("Bele bir islem yoxdur")
        continue
        
    