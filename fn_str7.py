hikaye = """kırmızı başlıklı kız bir gün
ormanda yürürken karşısına
bir kurt çıkmış. Kurt kıza demiş ki 
nereye gidiyorsun böyle kırmızı başlıklı kız
vs. vs. vs."""
print(hikaye.startswith("kırmızı", 0, 80))
print(str.endswith(hikaye, "pancar", 8 , 80))

bayi_kodu ="M123AB TEST ÖRNEK"
print(bayi_kodu.endswith("ST", 0, 11))