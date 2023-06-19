a = "abcdef\u00e8"
print(0xe8)
print(a)
print(a.isascii())

b = "aghk\u023A"
print(b.isalpha())
print(b)

c ="\u030C"
print(c)
print(c.isalnum())

d = "  D "
print(d)
print(d.isspace())

e = "kadirzey"
print(e.isalpha())