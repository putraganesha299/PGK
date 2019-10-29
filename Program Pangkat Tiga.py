#################################
# nama file: program perkalian.py
#################################

def main():
    # menggunakan prompt untuk tipe data integer
    bilanganbulat = int(input("masukkan bilangan bulat: "))

    # menggunakan variabel untuk melakukan hasil perhitungan
    hasil = bilanganbulat**3

    # menampilkan nilai variabel
    print("bilangan yang dimasukkan %d" % bilanganbulat)
    print("%d pangkat 3 = %d" % (bilanganbulat, hasil))

if __name__ == "__main__":
    main()
