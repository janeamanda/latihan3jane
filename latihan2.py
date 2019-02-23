print("Mencari bilangan Random, yang terhenti jika ketik angka 0")
max = 0
while True :
	a = int(input("Masukan bilangan :"))
	if max < a :
		max = a
	if a ==0:
		break
print('bilangan paling besar : ',max)
