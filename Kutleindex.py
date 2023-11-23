print("Kutle Indeksini Degerlendirme")

kilo =int(input("Kilonuz:"))
boy =float(input("Boyunuz:"))

index=float(kilo/(boy**2))

if index < 18.5:
    print("Ariq")
elif (index > 18.5 and index < 25):
    print("Normal")
elif (index > 25 and index < 30):
    print("Kilolu")
else:
    print("Obez")