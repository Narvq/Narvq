from colorama import init, Fore, Back, Style
init(autoreset=True)
print(Fore.BLUE + Style.BRIGHT + "====•===========WELCOME TO PROJECT=================•====\n Creator by Narvqey\n Version : 0.1\n © copyright by narvqey \n============================≈==≈=======================")

from colorama import init, Fore, Back, Style
init(autoreset=True)
print(Fore.CYAN + Style.BRIGHT + "Sistem and game\n •Kalkulator\n •Game biasa\n ")
pesan = input("Masukan game yg mau di mainkan : ")
if pesan.lower() == "kalkulator":
	angka1 = float(input("Masukan angka1 : "))
	angka2 = float(input("Masukan angka2 : "))
	tambah = angka1 + angka2
	perkalian = angka1 * angka2
	pengurangan = angka1 - angka2
	pembagian = angka1 / angka2
	print("Hasil penambahan : ", tambah)
	print("hasil perkalian : ", perkalian)
	print("Hasil pengurangan : ", pengurangan)
	print("hasil pembagian : ", pembagian)
	
elif pesan.lower() == "game biasa":
	import random

maxn = 10
n = random.randint(1, maxn)
print('Welcome to guess the number game!')
print('Guess the number from 1 to %d' % maxn)
guess = None
while guess != n:
    guess = int(input('Your try: '))
    if guess > n:
        print('Too high')
    if guess < n:
        print('Too low')

print('Congratulations, you won!')
