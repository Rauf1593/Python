print(""""***************************
      GIRIS
      ****************************""")


qlogin="rauf159"
qparol="men123"

login=input("Log in:")
parol=input("Parol:")

if (login == qlogin and parol != qparol):
    print("Parol duzgen deyil...")
elif (login != qlogin and parol == qparol):
    print("Giris adi duzgen deyil..")
elif (login != qlogin and parol != qparol):
    print("Login ve parol duzgen deyil..")
else:
    print("Giris ugurla bitti.")
