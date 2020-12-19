import sys
import os
import math
import time

print ("\nTeks Perulangan di dalam perulangan")

kode = int(input("\nMasukkan Nilai Perulangan : "))
a = int(input(("\nMasukkan nilai a:  ")))
b = int(input("\nMasukkan Nilai b:  "))
c = int(input("\nMasukkan Nilai c:  "))
D = (b*b) - (4*a*c)

x1 = D 
if x1 < 0 :
        print ("\nx1 adalah akar imajiner" * kode)
elif D == 0 :
        print ("\nHasil x1 ini adalah D = 0")
        x1 = (-b + math.sqrt(D)) / (2*a)
else:
        print ("\nHasil x1 ini adalah D > 0")
        x1 = (-b + math.sqrt(D)) / (2*a)
          

x2 = D 
if x2 < 0:
        print ("\nx2 adalah akar imajiner" * kode)
elif D == 0 :
        print ("\nHasil x2 ini adalah D = 0")
        x2 = x1
else:
        print ("\nHasil x2 ini adalah D > 0 ")
        x2 = (-b - math.sqrt(D)) / (2*a)        



#f = a + b * c
hitung = 0
jawab = "ya"
begin = time.time() 

for i in range(kode):
        #hitung +=1

        print ("\nHasil dari persamaan kuadrat dari " , (a) , (b), "dan", (c) ,"adalah", (x1) , "dan" ,(x2) )




for j in range(i):
        for k in range(kode):
                print("\nHasil dari persamaan kuadrat dari " , (a) , (b), "dan", (c) ,"adalah", (x1) , "dan" ,(x2))

        jawab = input("Ulangi lagi kah? ")
        hitung +=1
                
        if jawab != "ya":
                break

time.sleep(1) 
# store end time 
end = time.time()

print(f"Total jalannya waktu program adalah {end - begin}") 
print ('Total Perulangan ', str(kode))
print ('Total Perulangan sebanyak ', str(hitung))




