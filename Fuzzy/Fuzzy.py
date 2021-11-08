import pandas


#fuzifikasi
buruk = 0
sedang = 0
baik =  0
tidak_enak = 0
enak = 0
enak_sekali = 0
list_kualitas_restoran = []

restoran = pandas.read_csv('dataset/restoran.csv')
restoran_makanan = list(restoran['makanan'])
restoran_pelayanan = list(restoran['pelayanan'])
restoran_id = list(restoran['id'])



def hitung_kualitas_pelayanan(kualitas_pelayanan):
    global buruk, sedang, baik
    if kualitas_pelayanan <= 30:
        buruk = 1
    elif kualitas_pelayanan > 30 and kualitas_pelayanan < 40:
        sedang = (kualitas_pelayanan - 30)/(10)
        buruk = -(kualitas_pelayanan - 40)/(10)
    elif kualitas_pelayanan >= 40 and kualitas_pelayanan <= 70:
        sedang = 1
    elif kualitas_pelayanan > 70 and kualitas_pelayanan < 80:
        baik = (kualitas_pelayanan - 70)/(10)
        sedang = -(kualitas_pelayanan - 80)/(10)
    elif kualitas_pelayanan >= 80:
        baik = 1


def hitung_kualitas_makanan(kualitas_makanan):
    global tidak_enak, enak, enak_sekali
    if kualitas_makanan <= 3:
        tidak_enak = 1
    elif kualitas_makanan > 3 and kualitas_makanan < 4:
        enak = (kualitas_makanan - 3)/(1)
        tidak_enak = -(kualitas_makanan - 4)/(1)
    elif kualitas_makanan >= 4 and kualitas_makanan <= 7:
        enak  = 1
    elif kualitas_makanan > 7 and kualitas_makanan < 8:
        enak_sekali = (kualitas_makanan - 7)/(1)
        enak = -(kualitas_makanan - 8)/(1)
    elif kualitas_makanan >= 8:
        enak_sekali = 1



#fuzzy inference
kualitas_restoran_tmp = []
def fungsiInferensiBuruk(pelayanan, makanan):
    global kualitas_restoran_tmp
    if(pelayanan != 0 and makanan != 0):
        hasil = min(pelayanan,makanan)
        kualitas_restoran_tmp.append([hasil, 40])

def fungsiInferensiSedang(pelayanan, makanan):
    global kualitas_restoran_tmp
    if(pelayanan != 0 and makanan != 0):
        hasil = min(pelayanan,makanan)
        kualitas_restoran_tmp.append([hasil, 60])

def fungsiInferensiBaik(pelayanan, makanan):
    global kualitas_restoran_tmp
    if(pelayanan != 0 and makanan != 0):
        hasil = min(pelayanan,makanan)
        kualitas_restoran_tmp.append([hasil, 100])



def hitungInferensi(kualitas_makanan, kualitas_pelayanan):
    hitung_kualitas_makanan(kualitas_makanan)
    hitung_kualitas_pelayanan(kualitas_pelayanan)
    # print(buruk, tidak_enak, sedang, enak, baik, enak)
    fungsiInferensiBuruk(buruk, tidak_enak)
    fungsiInferensiBuruk(buruk, enak)
    fungsiInferensiBuruk(sedang, tidak_enak)
    fungsiInferensiSedang(buruk, enak_sekali)
    fungsiInferensiSedang(baik, tidak_enak)
    fungsiInferensiSedang(sedang, enak)
    fungsiInferensiBaik(sedang, enak_sekali)
    fungsiInferensiBaik(baik, enak)
    fungsiInferensiBaik(baik, enak_sekali)



#defuzifikasi
def defuzifikasi():
    pengali = 0
    pembagi = 0
    for j in range(0, len(kualitas_restoran_tmp)):
        perkalian = kualitas_restoran_tmp[j][0]*kualitas_restoran_tmp[j][1]
        pembagian = kualitas_restoran_tmp[j][0]
        pengali = pengali + perkalian
        pembagi = pembagian + pembagi
    z = (perkalian / pembagi)
    return z  


for i in range(0, len(restoran_id)):
    buruk = 0
    sedang = 0
    baik = 0
    enak = 0
    tidak_enak = 0
    enak_sekali = 0
    hitungInferensi(restoran_makanan[i], restoran_pelayanan[i])
    nilai = defuzifikasi()
    list_kualitas_restoran.append([restoran_id[i], nilai])
    kualitas_restoran_tmp = []

hasil_akhir = sorted(list_kualitas_restoran, reverse = True, key=lambda x: x[1])
list_rating = [x[1] for x in hasil_akhir]
list_id = [x[0] for x in hasil_akhir]
hasil_csv = {'ID restoran': list_id[:10], 'Rating': list_rating[:10]}

result_csv = pandas.DataFrame(hasil_csv, columns= ['ID restoran', 'Rating'])
result_csv.to_csv('dataset/result.csv')
print(list_kualitas_restoran)


