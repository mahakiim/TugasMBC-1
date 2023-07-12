#fungsi perjumlahan
def penjumlahan(x,y):
    return x+y

#fungsi pengurangan
def pengurangan(x,y):
    return x-y

#fungsi perkalian
def perkalian(x,y):
    return x*y

#fungsi pembagian
def pembagian(x,y):
    return x/y
print("==== Kalkulator Sederhana ====")
print()
print("Pilih operasi  :")
print("1. Perkalian")
print("2. Pengurangan")
print("3. Pertambahan")
print("4. Pembagian")
print("=========================")
print()

#input

pilihan = input("Pilih operasi :")

a = float(input("Masukkan bilangan pertama : "))
b = float(input("Masukkan bilangan kedua : "))

if pilihan == '1':
    print("Hasil dari ",a,"*",b,"=",perkalian(a,b))
    
elif pilihan == '2':
    print("Hasil dari ",a,"-",b,"=",pengurangan(a,b))
    
elif pilihan == '3':
    print("Hasil dari ",a,"+",b,"=",penjumlahan(a,b))
    
elif pilihan == '4':
    print("Hasil dari ",a,"/",b,"=",pembagian(a,b))
    
else:
    print("input salah")