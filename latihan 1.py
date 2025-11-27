import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))

print("Hasil a(5) =", a(5))
print("Hasil b(3, 4) =", b(3, 4))
print("Hasil c(2, 4, 6, 8) =", c(2, 4, 6, 8))
print("Hasil d('hello') =", d("hello"))       
