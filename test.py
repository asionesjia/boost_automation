def a():
    b = []
    c = 1
    d = yield c
    c = 2
    return c


print(a())
print(next(a()))
print(a())
print(a().send(5))
print(a())
print(a())
print(a())
print(a())
