import math

r = float(input(" Masukkan panjang jari-jari tabung: "))
t = float(input(" Masukkan tinggi tabung: "))

v = math.pi * r * r * t 

print("Volume tabung dengan jari-jari", r, "dan tinggi", t, "adalah", v)