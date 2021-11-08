import random
import math

batas_bawah_x = -1
batas_atas_x = 2
batas_bawah_y = -1
batas_atas_y = 1



def printPopulasi(populasi):
    for individu in populasi:
        print('Bit : ',individu.bit)
        print('Nilai X : ',individu.x)
        print('Nilai Y : ',individu.y)
        print('Nilai Fitness : ',fitness(individu.x, individu.y))
        print('\n')
    print('----------End of List-------------\n')


class Chromosom:
    def __init__(self, bit = None):
        if bit == None:
            self.bit = random.choices([0, 1], k=10)
        else:
            self.bit = bit
        self.x = self.decode(batas_atas_x, batas_bawah_x, self.bit[:5])
        self.y = self.decode(batas_atas_y, batas_bawah_y, self.bit[5:])
    

    def decode(self, ra, rb, g):
        pangkatDua = [2**-1 for i in range(1, len(g) + 1)]
        return rb + ((ra - rb) / sum(pangkatDua) * sum([g[i] * pangkatDua[i] for i in range(len(g))]))
    


def fitness(x, y):
    cosXSqrt = math.cos(x*x)
    sinYSqrt = math.sin(y*y)
    return (cosXSqrt * sinYSqrt) + (x + y)




def buatPopulasi():
    populasi = []
    while (len(populasi) != 10):
        individu = Chromosom()
        populasi.append(individu)
    
    return populasi






def seleksi_orang_tua(k, populasi):
    list_orang_tua = []
    list_fitness = list(map(lambda individu : fitness(individu.x, individu.y), populasi))
    list_weight = [list_fitness[i] / sum(list_fitness) for i in range(len(populasi))]
    while len(list_orang_tua) != k:
        kandidat = random.choices(populasi, weights=list_weight)[0] 
        list_orang_tua.append(kandidat)

    return list_orang_tua


def kawinSilang(orang_tua_1, orang_tua_2, populasi, peluang_mutasi):
    titik_potong = random.randint(1, len(orang_tua_1.bit) - 1)
    bit_anak_1 = orang_tua_1.bit[:titik_potong] + orang_tua_2.bit[titik_potong:]
    bit_anak_2 = orang_tua_2.bit[:titik_potong] + orang_tua_1.bit[titik_potong:]
    bit_anak_1 = mutasi(bit_anak_1, peluang_mutasi)
    bit_anak_2 = mutasi(bit_anak_2, peluang_mutasi)
    anak_1 = Chromosom(bit_anak_1)
    anak_2 = Chromosom(bit_anak_2)
    populasi.append(anak_1)
    populasi.append(anak_2)


def mutasi(individu, peluang):
    if peluang > random.random():
        posisi_mutasi = random.randint(0, len(individu) - 1)
        if individu[posisi_mutasi] == 0:
            individu[posisi_mutasi] = 1
        else:
            individu[posisi_mutasi] = 0
    return individu


def seleksi_survivor(populasi):
    n = 2
    populasi.sort(key = lambda individu : fitness(individu.x, individu.y), reverse =True)
    for i in range(n):
        populasi.pop()
    
    


populasi = buatPopulasi()
printPopulasi(populasi)
generasi = 1
print('Generasi ke : ', generasi)


while generasi <= 100:
    print('Generasi ke : ', generasi)
    orang_tua = seleksi_orang_tua(2, populasi)
    kawinSilang(orang_tua[0], orang_tua[1], populasi, 0.3)
    seleksi_survivor(populasi)
    printPopulasi(populasi)
    generasi += 1




