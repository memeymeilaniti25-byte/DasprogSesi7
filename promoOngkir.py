total_belanja = int(input("Masukkan total belanja: "))
ongkir= int(input("Masukkan Harga Ongkir: "))
status_member= input("Member Premium? True/False: ").lower() == 'true'
hari = input("Hari Transaksi: ").lower()

#potongan ongkir
if total_belanja >= 400000:
    persen_potongan_ongkir = 1.0
    print("Gratis Ongkir")
elif total_belanja >= 200000:
    persen_potongan_ongkir = 0.75
    print("Mendapat Potongan Ongkir 75%")    
elif total_belanja >= 150000:
    persen_potongan_ongkir = 0.5
    print("Mendapatkan Potongan Ongkir 50%")
else:
    persen_potongan_ongkir = 0.0
    print("Tidak Mendapatkan Potongan Ongkir")   

potongan_ongkir = ongkir * persen_potongan_ongkir
total_ongkir = ongkir - potongan_ongkir

#Cashback
cashback_persen = 0
if total_belanja >= 30000:
    casback_persen = 10
    print("Mendapatkan Cashback 10%")
elif total_belanja >= 200000:
    casback_persen = 7
    print("Mendapatkan Cashback 7%")
elif total_belanja >= 10000:
    casback_persen = 5
    print("Mendapatkan Cashback 5%")
else:
    print("Tidak Mendapatkan Cashback")    

#aturan tambahan cashback     
if status_member :
    cashback_persen += 5
if hari == "Sabtu":
    cashback_persen += 3
if cashback_persen > 15:
    cashback_persen = 15    

total_cashback = (cashback_persen / 100)* total_belanja
total_bayar = total_belanja + total_ongkir

print("/n---Transaksi---")
print(f"Potongan Ongkir : Rp{potongan_ongkir: },({persen_potongan_ongkir*100: }%)")
print(f"Ongkir yang Dibayar: Rp{total_ongkir: } ")
print(f"Persen Cashback: {cashback_persen}%")
print(f"Total Cashback (Rp): Rp {total_cashback: }")
print(f"Total Bayar: Rp {total_bayar: }")
 


        
