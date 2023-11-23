def ekob(e1, e2):
    i = max(e1, e2) 
    while True:
        if (i % e1 == 0) and (i % e2 == 0):
            return i 
        i += 1

eded1 = int(input("Eded1: "))
eded2 = int(input("Eded2: "))

print("Ekob:", ekob(eded1, eded2))