n = int(input('Masukkan jumlah kategori: '))
data_aplikasi = {}

for i in range(n):
    nama_kategori = input('Masukkan nama kategori:')
    print(f'Masukkan 5 nama aplikasi di kategori {nama_kategori}')

    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)

    data_aplikasi[nama_kategori] = aplikasi

print(data_aplikasi)

daftar_aplikasi_list = [set(aplikasi) for aplikasi in data_aplikasi.values()]

hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])

print("Aplikasi yang hanya muncul di satu kategori saja:")
for aplikasi in hasil:
    print(aplikasi)

if n > 2:
    print("\nAplikasi yang muncul tepat di dua kategori sekaligus:")
    for aplikasi in hasil:
        count = 0
        for kategori in data_aplikasi:
            if aplikasi in data_aplikasi[kategori]:
                count += 1
        if count == 2:
            print(aplikasi)
