Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Muhammad Rizqi Erdyansyah'
>>> NIM = 171
>>> Tinggi = 1.75
>>> Berat = 95
>>> TahunLahir = 2000
>>> Aku = (Tahunlahir, Berat, Tinggi, NIM, Nama)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    Aku = (Tahunlahir, Berat, Tinggi, NIM, Nama)
NameError: name 'Tahunlahir' is not defined
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> type (Aku)
<type 'tuple'>
>>> ## Aku merupakan data tuple
>>> Aku [0]
2000
>>> ## mnampilkan isi dari Aku data ke 0 yaitu tahun lahir
>>> a = NIM % 4; Aku[a]
171
>>> type (Aku[a])
<type 'int'>
>>> Aku[a:4]
(171,)
>>> a = NIM % 4; Aku[a]
171
>>> type (Aku[4])
<type 'str'>
>>> Aku[0]= 'ok'

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    Aku[0]= 'ok'
TypeError: 'tuple' object does not support item assignment
>>> type (Data)
<type 'tuple'>
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type (Data)
<type 'list'>
>>> type (Data[4])
<type 'str'>
>>> Data [4][5]
'm'
>>> Data[4][a:6]
'amm'
>>> Data [0] = 'ok' ; Data
['ok', 95, 1.75, 171, 'Muhammad Rizqi Erdyansyah']
>>> Data [-a]
1.75
>>> range(a)
[0, 1, 2]
>>> 
