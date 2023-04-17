pmt_b = 5000
pmt_k = 1000
psd_b = 600
psd_k = 100
prd_max = 7000
prd_min = 2000

x = int(input("Masukkan jumlah permintaan\t: "))
y = int(input("Masukkan jumlah Persediaan\t: "))

#Permintaan Naik--> Linear naik
if x<pmt_k:
    miu_pmt_naik = 0
elif x>=pmt_k and x <= pmt_b:
    miu_pmt_naik = (x-pmt_k)/(pmt_b-pmt_k)
else :
    miu_pmt_naik = 1

#Pemintaan Turun --> Linear Turun
if x<pmt_k:
    miu_pmt_turun = 1
elif x>=pmt_k and x <= pmt_b:
    miu_pmt_turun = (pmt_b-x)/(pmt_b-pmt_k)
else :
    miu_pmt_turun = 0

#Persediaan Sedikit --> Linear Turun
if y<psd_k:
    miu_psd_sedikit = 1
elif y>=psd_k and y<= psd_b:
    miu_psd_sedikit = (psd_b-y)/(psd_b-psd_k)
else :
    miu_psd_sedikit = 0

#Persediaan Banyak --> Linear Naik
if y<psd_k:
    miu_psd_banyak = 0
elif y>=psd_k and y<= psd_b:
    miu_psd_banyak = (y-psd_k)/(psd_b-psd_k)
else :
    miu_psd_banyak = 1

print("Nilai Derajat Keanggotaan Permintaan Naik\t",miu_pmt_naik)
print("Nilai Derajat Keanggotaan Permintaan Turun\t",miu_pmt_turun)
print("Nilai Derajat Keanggotaan Persediaan Sedikit\t",miu_psd_sedikit)
print("Nilai Derajat Keanggotaan Persediaan Banyak\t",miu_psd_banyak)
print("")

#Rule
def r1():
    r1=min(miu_pmt_naik,miu_psd_banyak)
    return r1

def r2():
    r2=min(miu_pmt_turun,miu_psd_sedikit)
    return r2

def r3():
    r3=min(miu_pmt_turun,miu_psd_banyak)
    return r3

def r4():
    r4=min(miu_pmt_naik,miu_psd_sedikit)
    return r4

#Rule 1 --> Produksi Barang Bertambah
z1 = (r1()*(prd_max-prd_min))+prd_min
print("Z1\t",z1)

#Rule 2 --> Produksi Barang Berkurang
z2 = prd_max-(r2()*(prd_max-prd_min))
print("Z2\t",z2)

#Rule 3 --> Produksi Barang Berkurang
z3 = prd_max-(r3()*(prd_max-prd_min))
print("Z3\t",z3)

#Rule 4 --> Produksi Barang Berkurang
z4 = (r4()*(prd_max-prd_min))+prd_min
print("Z4\t",z4)

#z Akhir
z_akhir = (r1()*z1+r2()*z2+r3()*z3+r4()*z4)/(r1()+r2()+r3()+r4())
print("Jumlah Produksi Barang",round(z_akhir))
