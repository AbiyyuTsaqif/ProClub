import collections

list_angka = list(map(str, input().split()))

def Jumlah_Kemunculan(List):
    counting = collections.Counter(List)
    sorted_dict = {}
    sorted_keys = sorted(counting, key=counting.get)  
    for w in sorted_keys:
        sorted_dict[w] = counting[w]
    return sorted_dict

spasi = Jumlah_Kemunculan(list_angka)
for i in spasi:
    print(i, ":", spasi[i])