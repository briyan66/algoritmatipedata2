# Input data pendaftar
nama = input("Masukkan nama Anda: ")
usia = int(input("Masukkan usia Anda: "))
pengalaman_kerja = int(input("Masukkan tahun pengalaman kerja Anda: "))

# Persyaratan
persyaratan_usia = 20
persyaratan_pengalaman_kerja = 3

# Proses seleksi
if usia >= persyaratan_usia and pengalaman_kerja >= persyaratan_pengalaman_kerja:
    print(f"Selamat, {nama}! Anda lolos seleksi.")
else:
    print(f"Mohon maaf, {nama}. Anda belum memenuhi persyaratan untuk melamar pekerjaan ini.")