print(pow(2, 3))

sayi = 1.5
kuvvet = 3
sonuc = pow(sayi, kuvvet)
print("%.2f sayısının %f kuvveti %.3f" % (sayi, kuvvet, sonuc))

sayi2 = 11
sayi3= 3
sonuc2 = divmod(sayi2, sayi3)
print(sonuc2[0], sonuc2[1])

sayi4 = -15
print(abs(sayi4))

sayi5 = 3.514
sonuc3 = round(sayi5, 2)
sonuc4 = round(sayi5, 1)
print((sonuc4))
print(sonuc3, type(sonuc3))

print(min(10, 26, 56, 6, 25))
print(max(14, 65, 67, 889, 45))