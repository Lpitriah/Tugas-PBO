print("Konversi Suhu Kelvin")

# Entry
suhu = (input("Masukkan suhu dalam kelvin: "))

# rumus
C = ((float(suhu)-273))
F = (9/5 * (float(suhu)-273) + 32)
R = (4/5 * (float(suhu)-273 ))

# output
print(str(suhu) + " Kelvin sama dengan ")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")