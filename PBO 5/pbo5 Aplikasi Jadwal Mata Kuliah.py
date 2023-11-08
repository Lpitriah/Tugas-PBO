import tkinter as tk

# Fungsi untuk menampilkan jadwal mata kuliah berdasarkan input hari
def tampilkan_jadwal():
    hari = input_hari.get().lower()  # Mengubah input menjadi huruf kecil
    jadwal = {
        "senin": [
            {"Mata_Kuliah": "Arsitektur dan Organisasi Komputer", "Waktu": "08.00-10.00"},
            {"Mata_Kuliah": "AIK", "Waktu": "10.00-11.40"}
        ],
        "selasa": [
            {"Mata_Kuliah": "PBO", "Waktu": "13.00-15.30"}
        ],
        "rabu": [
            {"Mata_Kuliah": "Kalkulus", "Waktu": "08.00-10.00"},
            {"Mata_Kuliah": "Sistem Informasi (APSI)", "Waktu": "13.00-15.30"}
        ],
        "kamis": [
            {"Mata_Kuliah": "Libur"}
        ],
        "jumat": [
            {"Mata_Kuliah": "Komunikasi Data", "Waktu": "10.00-11.40"},
            {"Mata_Kuliah": "Statistika dan Probabilitas", "Waktu": "13.00-14.40"},
            {"Mata_Kuliah": "Struktur Data", "Waktu": "15.00-17.30"}
        ]
    }
    jadwal_hari = jadwal.get(hari, [{"Mata_Kuliah": "Tidak ada mata kuliah"}])
    
    # Mengosongkan teks sebelum menampilkan jadwal baru
    text_jadwal.delete(1.0, tk.END)
    
    for mata in jadwal_hari:
        if 'Waktu' in mata:
            text_jadwal.insert(tk.END, f"{mata['Mata_Kuliah']} ({mata['Waktu']})\n")
        else:
            text_jadwal.insert(tk.END, f"{mata['Mata_Kuliah']}\n")

# Membuat jendela utama
root = tk.Tk()
root.title("Jadwal Mata Kuliah")

# Membuat elemen-elemen UI
label = tk.Label(root, text="Masukkan hari:")
label.pack()

input_hari = tk.Entry(root)
input_hari.pack()

tampilkan_button = tk.Button(root, text="Tampilkan Jadwal", command=tampilkan_jadwal)
tampilkan_button.pack()

text_jadwal = tk.Text(root, width=70, height=10)
text_jadwal.pack()

label_nama = tk.Label(root, text="Laelatul Pitriah- 220511114:")
label_nama.pack()

# Menjalankan aplikasi
root.mainloop()






