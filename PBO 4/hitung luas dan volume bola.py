import tkinter as tk
from math import pi

# Fungsi untuk menghitung luas permukaan dan volume bola
def hitung():
    try:
        jari_jari = float(Entry_jari_jari.get())
        luas_permukaan = 4 * pi * jari_jari**2
        volume = (4/3) * pi * jari_jari**3
        hasil_luas_permukaan.set(f"Luas Permukaan: {luas_permukaan:.2f}")
        hasil_volume.set(f"Volume: {volume:.2f}")
    except ValueError:
        hasil_luas_permukaan.set("Masukkan angka valid")
        hasil_volume.set("Masukkan angka valid")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Bola")

#NAMA
label_nama = tk.Label(root, text="LAELATUL PITRIAH")
label_nama.pack()

# Membuat label untuk input jari-jari
label_jari_jari = tk.Label(root, text="Jari-jari bola:")
label_jari_jari.pack()

# Membuat entry (input field) untuk jari-jari bola
Entry_jari_jari = tk.Entry(root)
Entry_jari_jari.pack()

# Membuat tombol "Hitung"
hitung_button = tk.Button(root, text="Hitung", command=hitung)
hitung_button.pack()

# Variabel StringVar untuk menampilkan hasil perhitungan
hasil_luas_permukaan = tk.StringVar()
hasil_volume = tk.StringVar()

# Membuat label untuk menampilkan hasil
label_luas_permukaan = tk.Label(root, textvariable=hasil_luas_permukaan)
label_luas_permukaan.pack()

label_volume = tk.Label(root, textvariable=hasil_volume)
label_volume.pack()

# Menjalankan aplikasi
root.mainloop()