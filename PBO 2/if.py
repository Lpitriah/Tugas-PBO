print("Paket Combo Meal")
harga_beli = int(input("Masukkan total harga beli: "))

if harga_beli >= 120000:
    menu = "Paket Super Family =====> 5pcs chicken + 3 nasi + 3 cocacola"
elif harga_beli >= 47000:
    menu = "Paket Super Besar 2 =====> 2pcs chicken + nasi + cocacola"
elif harga_beli >= 35000:
    menu = "Paket Super Besar 1 ======> 2pcs chicken + nasi + cocacola"
elif harga_beli >= 22000:
    menu = "Paket Winger =====> 1pcs chicken + nasi + cocacola"
else:
    menu = "Anda tidak mendapatkan paket combo"

print(menu)