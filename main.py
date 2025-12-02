# 6
sonlar = [-5, 3, -2, 7]

modul = list(map(lambda x: abs(x), sonlar))
print(modul)

# 7
sozlar = ["salom", "python", "dars"]

teskari = list(map(lambda x: x[::-1], sozlar))
print(teskari)

# 8
sonlar = [1, 2, 3, 4]

kub = list(map(lambda x: x**3, sonlar))
print(kub)

# 9
sozlar = ["salom", "dunyo", "python"]

birinchi = list(map(lambda x: x[0], sozlar))
print(birinchi)

# 10
sonlar = [3, 10, 7, 4]

juft_toq = list(map(lambda x: "Juft" if x % 2 == 0 else "Toq", sonlar))
print(juft_toq)
