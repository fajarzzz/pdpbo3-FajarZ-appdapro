"""
   Author : Fajar Zuliansyah Trihutama
   NIM    : 1905394

   Saya Fajar Zuliansyah Trihutama bersumpah/berjanji mengerjakan TP3 
   dalam mata kuliah Desain dan Pemrograman Berorientasi Objek
   untuk keberkahanNya maka saya tidak melakukan kecurangan 
   seperti yang telah di spesifikasikan.
"""

from UI import Tampilan
from tkinter import *

# Main Program
if __name__ == '__main__':
   root = Tk()
   
   # call kelas tampilan
   app = Tampilan(root, "Main Window")

   root.mainloop()
