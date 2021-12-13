angka = input()

def angkamunculsekali(angka) :
    y = list()
    for i in set(angka):
        if list(angka).count(i) == 1:
            y.append(i)
    return y
print(sorted(angkamunculsekali(angka), reverse=True))