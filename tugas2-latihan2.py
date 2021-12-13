def penjumlahan_angka(angka, target):
    temp = list()
    for first in angka:
        for second in angka:
            if (first + second) == target:
                temp.extend([angka.index(first), angka.index(second)])
                return temp
    return []


list_angka = [int(x) for x in input().split()]
target = int(input())
print(penjumlahan_angka(list_angka, target))