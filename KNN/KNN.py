import pandas
import math

#import dataset
dataset = pandas.read_csv('dataset.csv')
list_nama_mobil = list(dataset['Nama Mobil'])
list_ukuran_mobil = list(dataset['Ukuran'])
list_kenyamanan_mobil = list(dataset['Kenyamanan'])
list_irit_mobil = list(dataset['Irit'])
list_kecepatan_mobil = list(dataset['Kecepatan'])
list_harga_mobil = list(dataset['Harga'])


#import data test
data_test = pandas.read_csv('test.csv')
harga_input = list(data_test['Ukuran'])[0]
ukuran_input = list(data_test['Kenyamanan'])[0]
kenyamanan_input = list(data_test['Irit'])[0]
irit_input = list(data_test['Kecepatan'])[0]
kecepatan_input = list(data_test['Harga'])[0]



#preprosesing / normalisasi
max_col_val = []
min_col_val = []
def normalize_dataset(df, column):
    global max_col_val
    global min_col_val
    result = df.copy()
    for col in column:
        max_value = df[col].max()
        min_value = df[col].min()
        max_col_val.append(max_value)
        min_col_val.append(min_value)
        result[col] = ((df[col] - min_value) / (max_value - min_value))
    return result


def normalize_test(df,column):
    result = df.copy()
    idx = 0
    for col in column:
        max_value = max_col_val[idx]
        min_value = min_col_val[idx]
        # print(int(df[col]))
        if int(df[col]) < min_value:
            min_value = int(df[col])
            min_col_val[idx] = int(df[col]) 
        if(int(df[col]) > max_value):
            max_value = int(df[col])
            max_col_val[idx] = int(df[col])
        result[col] = ((df[col] - min_value) / (max_value - min_value))
        idx += 1
    return result

column_list = ['Ukuran', 'Kenyamanan', 'Irit', 'Kecepatan', 'Harga']
dataset_normalization_result = normalize_dataset(dataset, column_list)
test_normalization_result = normalize_test(data_test, column_list)



list_ukuran_mobil = list(dataset_normalization_result['Ukuran'])
list_kenyamanan_mobil = list(dataset_normalization_result['Kenyamanan'])
list_irit_mobil = list(dataset_normalization_result['Irit'])
list_kecepatan_mobil = list(dataset_normalization_result['Kecepatan'])
list_harga_mobil = list(dataset_normalization_result['Harga'])


harga_input = list(test_normalization_result['Harga'])[0]
ukuran_input = list(test_normalization_result['Ukuran'])[0]
kenyamanan_input = list(test_normalization_result['Kenyamanan'])[0]
irit_input = list(test_normalization_result['Irit'])[0]
kecepatan_input = list(test_normalization_result['Kecepatan'])[0]



def calculateEuclidean(index):
    ukuran1 = list_ukuran_mobil[index]
    ukuran2 = ukuran_input
    ukuran = (ukuran1 - ukuran2)**2

    kenyaman1 = list_kenyamanan_mobil[index]
    kenyaman2 = kenyamanan_input
    kenyamanan = (kenyaman1 - kenyaman2)**2

    irit1 = list_irit_mobil[index]
    irit2 = irit_input
    irit = (irit1 - irit2)**2

    kecepatan1 = list_kecepatan_mobil[index]
    kecepatan2 = kecepatan_input
    kecepatan = (kecepatan1 - kecepatan2)**2

    harga1 = list_harga_mobil[index]
    harga2 = harga_input
    harga = (harga1 - harga2)**2

    euclideanDistance = math.sqrt(ukuran + kenyamanan + irit + kecepatan + harga)
    return euclideanDistance


def calculateManhattan(index):
    ukuran1 = list_ukuran_mobil[index]
    ukuran2 = ukuran_input
    ukuran = abs(ukuran1 - ukuran2)

    kenyaman1 = list_kenyamanan_mobil[index]
    kenyaman2 = kenyamanan_input
    kenyamanan = abs(kenyaman1-kenyaman2)

    irit1 = list_irit_mobil[index]
    irit2 = irit_input
    irit = abs(irit1-irit2)

    kecepatan1 = list_kecepatan_mobil[index]
    kecepatan2 = kecepatan_input
    kecepatan = abs(kecepatan1-kecepatan2)

    harga1 = list_harga_mobil[index]
    harga2 = harga_input
    harga = abs(harga1-harga2)

    manhattanDistance = ukuran+kenyamanan+irit+kecepatan+harga
    return manhattanDistance
    

def calculateMinkowski(index):
    h_val = 1.5

    ukuran1 = list_ukuran_mobil[index]
    ukuran2 = ukuran_input
    ukuran = abs(ukuran1 - ukuran2)**h_val

    kenyaman1 = list_kenyamanan_mobil[index]
    kenyaman2 = kenyamanan_input
    kenyamanan = abs(kenyaman1-kenyaman2)**h_val

    irit1 = list_irit_mobil[index]
    irit2 = irit_input
    irit = abs(irit1-irit2)**h_val

    kecepatan1 = list_kecepatan_mobil[index]
    kecepatan2 = kecepatan_input
    kecepatan = abs(kecepatan1-kecepatan2)**h_val

    harga1 = list_harga_mobil[index]
    harga2 = harga_input
    harga = abs(harga1-harga2)**h_val

    minkowskiDistance = (ukuran+kenyamanan+irit+kecepatan+harga)**(1/h_val)
    return minkowskiDistance
    
def calculateSupremum(index):
    ukuran1 = list_ukuran_mobil[index]
    ukuran2 = ukuran_input
    ukuran = abs(ukuran1 - ukuran2)

    kenyaman1 = list_kenyamanan_mobil[index]
    kenyaman2 = kenyamanan_input
    kenyamanan = abs(kenyaman1-kenyaman2)

    irit1 = list_irit_mobil[index]
    irit2 = irit_input
    irit = abs(irit1-irit2)

    kecepatan1 = list_kecepatan_mobil[index]
    kecepatan2 = kecepatan_input
    kecepatan = abs(kecepatan1-kecepatan2)

    harga1 = list_harga_mobil[index]
    harga2 = harga_input
    harga = abs(harga1-harga2)

    supremumDistance = max(ukuran, kenyamanan, irit, kecepatan, harga)
    return supremumDistance



def findAllDist(dist_calc_func):
    i = 0
    list_dist = []
    while i<len(list_nama_mobil):
        distance = dist_calc_func(i)
        list_dist.append([distance, list_nama_mobil[i]])
        i = i + 1
    list_dist.sort(key=lambda item: item[0])
    return list_dist


list_euclide_dist =  findAllDist(calculateEuclidean)
list_manhattan_dist = findAllDist(calculateManhattan)
list_minkowski_dist = findAllDist(calculateMinkowski)
list_supremum_dist = findAllDist(calculateSupremum)



def exportToCsv(prepared_list, used_dist):
    list_nama_mobil = [x[1] for x in prepared_list[:3]]
    header_csv = {'Rekomendasi mobil' : list_nama_mobil}
    result_csv = pandas.DataFrame(header_csv, columns=['Rekomendasi mobil'])
    result_csv.to_csv('rekomendasi_' + used_dist + '.csv')


exportToCsv(list_euclide_dist, 'Euclidean')
exportToCsv(list_manhattan_dist, 'Manhattan')
exportToCsv(list_minkowski_dist, 'Minkowski')
exportToCsv(list_supremum_dist, 'Supremum')





