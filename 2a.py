print("Перша константа", Ellipsis)
print("Друга константа", __debug__)

print (bool(10))
print (bin(10))

A = 4
print("Значить А>5" if A>5 else "Значить А<5")


B = "string"
try:
    print("Що буде якщо", 10/B, "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")

with open("README.md", "r") as f:
    for line in f:
        print(line)

x = lambda a : a + a
print(x(3))
