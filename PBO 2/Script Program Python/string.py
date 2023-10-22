nama_depan = "Laelatul"
nama_belakang = "Pitriah"

nama_lengkap=nama_depan + nama_belakang
print (nama_lengkap)

#menghitung panjang string
panjang = len (nama_lengkap)
print ("panjang dari" + nama_lengkap + "=" + str(panjang) )

#item paling kecil
print ("paling kecil :" + min (nama_lengkap))
#item paling besar
print ("paling kecil :" + max (nama_lengkap))

#Mengkapitalkan huruf pertama string
capitalized_nama_lengkap = nama_lengkap.capitalize()
print(capitalized_nama_lengkap)  

#Mengembalikan string yang dilapisi dengan fillchar dan dipusatkan pada total width kolom
centered_nama_lengkap = nama_lengkap.center(20, '*')
print(centered_nama_lengkap)  

# count(str, beg, end): Menghitung berapa kali str terjadi dalam string
count = nama_lengkap.count('l')
print(count)

# endswith(suffix, beg, end): Menentukan apakah string berakhir dengan akhiran
ends_with = nama_lengkap.endswith('Pitriah')
print(ends_with)

# expandtabs(tabsize): Memperluas tab dalam string ke banyak ruang
tabbed_nama_lengkap = "Lelatul\tPitriah!"
expanded_nama_lengkap = tabbed_nama_lengkap.expandtabs(4)
print(expanded_nama_lengkap) 

# find(str, beg, end): Mencari indeks pertama kali str terjadi dalam string
index = nama_lengkap.find('Pitriah')
print(index)  # Output: 7

# isalnum(): Mengembalikan true jika string alfanumerik
is_alphanumeric = nama_lengkap.isalnum()
print(is_alphanumeric)

# islower(): Mengembalikan true jika semua huruf dalam string adalah huruf kecil
is_lower = nama_lengkap.islower()
print(is_lower)

# join(seq): Menggabungkan elemen dalam urutan menjadi string dengan pemisah
words = ['Laelatul', 'Pitriah']
joined_nama_lengkap = ' '.join(words)
print(joined_nama_lengkap)

# lower(): Mengonversi huruf besar menjadi huruf kecil
lower_nama_lengkap = nama_lengkap.lower()
print(lower_nama_lengkap) 

# upper(): Mengonversi huruf kecil menjadi huruf besar
upper_nama_lengkap = nama_lengkap.upper()
print(upper_nama_lengkap) 