a= 0b00_00_00_11
c = 0b00_11_00_00
print(a)

b = a << 4
print(b)
print(bin(b))


d =248
print(bin(d))

e = d >> 4
print(bin(e))
print(e)

f = 0b00_11_11_00 # 60
g = 0b00_00_11_01 # 13
h = f & g
print(h, bin(h))

z = 0b111101 #61
