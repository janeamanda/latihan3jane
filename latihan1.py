print('====== Bilangan Acak Yang Lebih Kecil Dari 0.5 ======')
print('')
import random
N = int(input("Masukan nilai N : "))
a = 0
for x in range(N):
	a +=1
	b = random.uniform(0.0,0.5)
	print('Data ke :',a, '==>',b)
print("***SELESAI***")
print('')
jawab = "lanjut"
hitung =0
while jawab == "lanjut":
	hitung +=1
	jawab = input('Pengulangan?(yes/no) :')
	if jawab == "lanjut":
		break
print('Total perulangan :' + srt(hitung))
