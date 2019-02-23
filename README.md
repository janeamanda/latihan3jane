#latihan3jane
**Mencari bilangan Random, dari angka 0.0 hingga 0.5**
-----------------------------------------------------------------------------------------------------------------------------
*Seperti ini algoritmanya**

import random :: Untuk mengambil bilangan random,

N = int(input("Masukan nilai N : ")) // menangkap variabel dengan huruf N, dan mendata untuk integer

for x in range(n) // melooping sebuah bilang x dengan variabel yg sudah ada

b = random.uniform(0.0,0.5) // membuat bilangan random yang menghasilkan 0.0 s/d 0.5

print ("Data ke : ",a,"==>",b) ,, print data ke : a = index looping b = angka random yang sudah di buat varibelnya

print("Selesai") // membuat kata akhir setelah dikerjakan yang akan muncul " Hasil"

while jawab == "lanjutkan" // itu menandakan bahwa perulangan terjadi 8._ Hitung +=1 // itu mengubah atau menambahkan dari bilangan 

hitung = 0

if jawab == "lanjuttkan" : // hanya jika menjawab bilangan

break // untuk berrhenti jika ada syntax yang ia berikan.

-Codingan 
```
print('====== Bilangan Acak Yang Lebih Kecil Dari 0.5 ======')
    print(' ')
    import random
    N = int(input("Masukan nilai N : "))
    a = 0
    for x in range(N):
        a += 1
        b = random.uniform(.0,.5)
        print('Data ke:',a,'==>',b)
    print('Selesai')
    print('')
    jawab = 'lanjutkan'
    hitung = 0
    while jawab == "lanjutkan":
        hitung += 1
        jawab = input('Ingin Mengulang? (yes/no) : ')
        if jawab == "Lanjutkan":
            break
    print('Total perulangan : ' + str (hitung))
```

hasil :

<img width="375" alt="gmbrjane1" src="https://user-images.githubusercontent.com/46948060/53283678-69158080-377c-11e9-8bc8-b432bfcd69de.PNG">

**Mencari bilangan terbesar, yang terhenti bila diketik angka 0**

--------------------------------------------------------------------------------------------------------------------
-Algoritma

Max = 0 // variabel akhir random 0

While True // Perulangan Jika Benar

a = int(input("Masukan bilangan")) // untuk mengambil data dari integer dalam input yang akan dirandom

if max <a // jika si max lebih kecil dari a ia akan berhenti

if a ==0: // jika a == 0 dia berhenti memanggil

break // jika sudah dipanggil ia akan berhenti

print('bilangan paling besar : ',max)

Codingan
```
print("Mencari bilangan Random, yang terhenti jika ketik angka 0")
max = 0
while True :
  a = int(input("Masukan bilangan"))
  if max < a :
     max = a
  if a ==0:
     break
print('bilangan paling besar : ',max)

```

hasil :

<img width="353" alt="gmbrjane2" src="https://user-images.githubusercontent.com/46948060/53283679-69158080-377c-11e9-8caa-4ad11e51d188.PNG">


**Menghitung Laba karyawan***

Algoritma
a = 100.000.000 // variabel awalnya adalah 100000000
for i in range(1,9) // untuk membuat huruf i dengan jarak (1,9)
if(x>=1 and x<=2):- // jika x lebih besar = 1 dan kecil dari 2 ia akan menghasilkan bilangan seperti b=a*0
total=a+b+c+c+d+d+d+e // ini adalah hasilnya .
print("\nTotal :",total) // untuk mengetahui hasil
Codingan
print("Menghitung laba perusahaan dengan modal awal Rp 100.000.000")
print("")
print('note')
print('Bulan pertama dan ke 2 = 0%')
print('pada bulan ke 3 = 1%')
print('pada bulan ke 5 = 5%')
print('pada bulan ke 8 = 8%')
print("")

a = 100000000
for x in range(1,9):
        if(x>=1 and x<=2):
                b=a*0
                print("laba bulan ke - ",x, " : " ,b)
        if(x>=3 and x<=4):
                c=a*0.1
                print("laba bulan -",x, " : " ,c)
        if(x>=5 and x<=7):
                d=a*0.5
                print("laba bulan - ",x, " : " ,d)
        if(x==8):
                e=a*0.2
                print("laba bulan - ",x, " : " ,e)
total=a+b+c+c+d+d+d+e
print("\nTotal :",total)

hasil :

<img width="516" alt="gmbr3jane" src="https://user-images.githubusercontent.com/46948060/53283680-69158080-377c-11e9-8eb6-b9d2d7a3aab7.PNG">
