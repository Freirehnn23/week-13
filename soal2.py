data_list = [1, 2, 3, 4, 5, 1, 2, 3]
data_tuple = (1, 2, 3, 4, 5, 1, 2, 3)

data_set = set(data_list)
print("Data List Sebelum di Konversi Menjadi Data Set: ", data_list)
print("List ke Set:", data_set)  

data_list = list(data_set)
print("\nData List Sebelum di Konversi Menjadi Data Set", data_set)
print("Set ke List:", data_list)

data_set = set(data_tuple)
print("\nData Tuple Sebelum Dikonversi Menjadi set: ",data_tuple)
print("Tupel ke Set:", data_set)

data_tuple = tuple(data_set)
print ("\nData Set Sebelum Dikonversi Menjadi Tuple: ",data_set)
print("Set ke Tupel:", data_tuple)
