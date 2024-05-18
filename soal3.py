def baca_file(input_file):
    try:
        with open(input_file, 'r') as file:
            konten = file.read().lower()
        return konten
    except FileNotFoundError:
        print(f"File {input_file} tidak ditemukan.")
        return ""

def main():
    input_file1 = input("Masukkan path untuk file pertama: ")
    input_file2 = input("Masukkan path untuk file kedua: ")

    file1 = baca_file(input_file1)
    file2 = baca_file(input_file2)
    
    semua_konten = file1 + file2
    
    print("Konten dari kedua file adalah:")
    print(semua_konten)

if __name__ == "__main__":
    main()
