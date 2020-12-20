import sys
import os
import math

def main():

   jawab = 'ya'
   hitung = 0
  
   while True:
      hitung +=1
      print (user_math())
      jawab = input("Ulangi Lagi? ")
      
      #user_math()
      if jawab != 'ya':
         break

   print ("Total Perulangan = " , str(hitung))

def user_math():
   # Menampilkan judul program
   print ("\nPersamaan Kuadrat")

   # Meminta user memasukkan a b c
   a = int(input("\nMasukkan nilai a: "))
   b = int(input("Masukkan nilai b: "))
   c = int(input("Masukkan nilai c: "))

   # Hitung D
   D = (b*b) - (4*a*c)

   if D < 0:
      print ("akar-akar imajiner, exitting...")
      sys.exit(1) #exit program

   elif D == 0:
      x1 = (-b + math.sqrt(D)) / (2*a)
      x2 = x1

   else:
      x1 = (-b + math.sqrt(D)) / (2*a)
      x2 = (-b - math.sqrt(D)) / (2*a) 

   # Setelah nilai D dan akar-akar didapat, tampilkan hasil
   print ("\nx1 = %d" %x1 )
   print ("\nx2 = %d" %x2 )
   print ("\n")

   os.system("pause")

if __name__ == '__main__':
   main()
