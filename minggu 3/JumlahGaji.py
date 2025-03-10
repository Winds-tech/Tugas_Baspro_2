nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status(Pegawai Tetap/Honor): ").strip().lower()
golongan = input("Masukkan Golongan(A/B/C): ").strip().upper()

gaji_tetap = 1000000
bonus_tetap = {"A": 200000, "B": 400000, "C": 550000}

gaji_honor = 750000
bonus_honor = {"A": 150000, "B": 275000, "C": 480000}

if status == "pegawai tetap" :
    gaji = gaji_tetap
    bonus = bonus_tetap.get(golongan,0)  
elif status == "honor":
    gaji = gaji_honor
    bonus = bonus_honor.get(golongan,0)
else :
    print("Status tidak valid!")
    exit()

total_gaji = gaji + bonus

print("\n=== Rincian Gaji ===")
print("Nama: " + nama)
print("NIK: " + nik)
print("Status: " + status.capitalize())
print("Golongan: " + golongan)
print("Gaji Pokok: Rp " + format(gaji, ","))
print("Bonus: Rp " + format(bonus, ","))
print("Total Gaji: Rp " + format(total_gaji, ","))
