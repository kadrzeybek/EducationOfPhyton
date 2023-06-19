a = 5
b = 5
print(a is b)
print(id(a), id(b))

c = "kadir"
d ="kadir"
print(c is not d)
print(id(c), id(d))
print(type(c))
print(c != d)
print(type(d) is type(a))