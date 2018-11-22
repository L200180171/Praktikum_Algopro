#KEGIATAN 1

isi = {'nama' : 'Muh Rizqi E', 'nim' : 'L200180171', 'alamat' : 'solo', 'pro' : 'Informatika', 'kode pos' : '57113', 'pekerjaan' : 'mahasiswa', 'sosmed' : 'rizqi_erdy55'}
def nama():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('Nama :' + isi['nama'])
def nim() :
    "menampilkan data diri masing-masing 1 setiap data"
    print ('NIM :' + isi['nim'])
def alamat():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('Alamat :' + isi['alamat'])
def prd():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('Prodi :' + isi['pro'])
def kode():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('Kode pos :' + isi['kode pos'])
def kerja():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('Pekerjaan : ' + isi['pekerjaan'])
def sosmed():
    "menampilkan data diri masing-masing 1 setiap data"
    print ('Sosmed :' + isi['sosmed'])
def pilihan() :
        "menampilkan piihan yang tersedia"
        print ('pilihan yang tersedia :')
        print ('a. tampilkan Nama')
        print ('b. tampilkan NIM')
        print ('c. tampilkan Alamat')
        print ('d. tampilkan Prodi')
        print ('e. tampilkan Kode pos')
        print ('f. tampilkan pekerjaan')
        print ('g. tampilkan Sosmed')
        print ('B. Bantuan')
        print ('k. keluar')
        return ;

pilihan()
ulg = True
while ulg :
    y = raw_input('masukkan pilihan :')
    if y == 'a' :
        nama()
    elif y == 'b' :
        nim()
    elif y == 'c' :
        alamat()
    elif y == 'd' :
        prd()
    elif y == 'e' :
        kode()
    elif y == 'f' :
        kerja()
    elif y == 'g' :
        sosmed()
    elif y == 'B' :
        pilihan()
    elif y == 'k' :
        print "Terima Kasih."
        ulg = False

## KEGIATAN 2

def konversiSuhu (C=0, F=0) :
    "fungsi untuk mengkonversi suhu celcius dan farenheit"
    if C != 0 :
        y = ((9*C/5)+32)
        print 'Suhu', C, 'Celcius setara dengan', y, 'Farenheit'
    elif F != 0 :
        b = ((F-32)*5/9)
        print 'Suhu', F, 'Farenheit setara dengan', b, 'Celcius'
