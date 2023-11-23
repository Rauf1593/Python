print("""**********************************
1.Toplama

2. Cixma

3. Vurma

4. Bolme
**********************************""")

a= int(input("Birinci eded:"))
b= int(input("Ikinci eded:"))

islem= input("Isleminiz:")

if islem == "1":
    print("{} ile {} in cemi {} dir.".format(a,b,a+b))
elif islem == "2":
    print("{} ile {} in ferqi {} dir.".format(a,b,a-b))
elif islem == "3":
    print("{} ile {} in hasili {} dir.".format(a,b,a*b))
elif islem == "4":
    print("{} ile {} in qismeti {} dir.".format(a,b,a/b))
else:
    print("Dogru giriniz....")
    


    