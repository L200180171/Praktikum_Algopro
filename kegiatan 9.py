#keg 1
Data= open("L200180171", "w")
Data.write("L200180171, ""\n")
Data.write("05-10-2000, ""\n")
Data.write("Muhammad Rizqi Erdyansyah, ""\n")
Data.close()



#keg 2

Data= open("L200180171", "r")
nim = Data.readlines()
print (nim[2])
print "Surakarta, ",(nim[1])
print (nim[0])
Data.close()

#kegiatan 3

import shelve
a= open("L200180171", "r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
a.close()

#kegiatan 4

a = shelve.open('Erdy')
a['b'] = [NIM, TL, Nama]
print "NIM", "\t"," : ", "\t", a['b'][0]
print "TL","\t"," : ", "\t", a['b'][1]
print "Nama","\t"," : ","\t", a['b'][2]
a.close
