print(""" *****************
Giris
*****************""")

login = "arauf159"
parol = "yeruselim"
giris_sayi = 3
while True:
    sys_login = input("Log in:")
    sys_parol = input("Parol:")
    if (login == sys_login and parol != sys_parol):
        print("Parol sehvdir.")
        giris_sayi -= 1
    elif (login != sys_login and parol == sys_parol):
        print("Log in sehvdir.")
        giris_sayi -=1
    elif (login != sys_login and parol != sys_parol):
        print("Log in ve parol sehvdir.")
        giris_sayi -=1
    else:
        print("Giris ugurla yekunlasdi.")
        break
    if (giris_sayi == 0):
        print("Giris haqqiniz bitti...")
        break
     
    
