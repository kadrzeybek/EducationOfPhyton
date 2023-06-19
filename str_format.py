# print("Python {} {} bir dil.".format("çok", "güzel"))
# # a = input("Adınızı giriniz:")
# # print("Merhaba {}!".format(a.title()))

metin = "{2} {0} {1} {3}"
print(metin.format("çok", "güzel", "Python", "dil"))

metin2 = "{0:^16} {1:^8}  {2:<4.4}"
print(metin2.format("Ad Soyad", "No", "Ortalama"))
print(metin2.format("-" * 16, "-" * 8, "-" * 12))
print(metin2.format("Ali Çetin", "976", "65.25"))
"""
isim_soyisim = input("İsim ve Soyisminizi Giriniz:")
tc = input("TC Kimlik Numaranızı Giriniz:")
a = "{0: ^20} {1:^11.11s}"
print("Hasta".center(20), "Hastanın TC Kimlik Numarası".center(11))
print(a.format(isim_soyisim.title(), tc))
"""