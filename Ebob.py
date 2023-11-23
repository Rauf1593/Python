def ebob(e1,e2):
    i=1
    ebo=1
    while e1>=i and e2>=i:
        if (e1 % i==0) and (e2 % i == 0):
            ebo=i
        i+=1
    return ebo

eded1= int(input("Eded1:"))
eded2= int(input("Eded2:"))

print("Ebob:",ebob(eded1,eded2))