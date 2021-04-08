from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Produk import Produk
from PIL import ImageTk, Image

# kelas tampilan GUI
class Tampilan:
   # Konstruktor
   def __init__(self,root,title):
      self.win=root
      self.win.title(title)
      self.win.geometry("800x620")
      self.win.protocol("WM DELETE WINDOW", self.onClose)
      self.data = []

      self.set_widget()

   # fungsi saat ingin exit
   def onClose(self, event=None):
      response = messagebox.askquestion("Konfirmasi", "Anda akan keluar dari aplikasi?")
      if response == 'yes':
         self.win.destroy()

   # fungsi window detail produk
   def details(self,index):
      top = Toplevel()
      top.title("Detail " + self.data[index].getnama())

      d_frame = LabelFrame(top, text="Data Gambar {}".format(self.data[index].getnama()), padx=10, pady=10)
      d_frame.pack(side=TOP,padx=10, pady=10)
      
      detail_frame = LabelFrame(top, text="Data Detail {}".format(self.data[index].getnama()), padx=10, pady=10)
      detail_frame.pack(side=LEFT, padx=10, pady=10)
      
      try:
         # menampilkan gambar
         img = ImageTk.PhotoImage(Image.open(self.data[index].getpicture()))
         imgLb = Label(d_frame, image=img)
         imgLb.pack(side=TOP)
      except:
         messagebox.showinfo("Warning", "Gagal menampilkan gambar")

      # menampilkan detail lain dari sisa atribut
      hjual=Label(detail_frame, text="Harga Jual : " + self.data[index].gethJual(), justify=LEFT, anchor ="w")
      hjual.pack(side=TOP)

      hbeli=Label(detail_frame, text="Harga Beli : " + self.data[index].gethBeli(), justify=LEFT, anchor ="w")
      hbeli.pack(side=TOP)
      i=1
      for item in self.data[index].gettambahan():
         if(str(item.get()) != "N"):
            tambahan = Label(detail_frame, text="Tambahan : "+ str(i) +". "+ str(item.get()), justify=LEFT, anchor ="w")
            tambahan.pack(side=TOP)
            i+=1

   # membuka file gambar  
   def openFile(self, frame):
      # select image
      self.win.filename = filedialog.askopenfilename(initialdir = "/", title="Select a File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
      imageLb = Label(frame, text=self.win.filename, font=('Helvetica', 9, 'italic')).grid(row=12, column=3, columnspan=2)

   # buka window about
   def openAbout(self, title):
      top = Toplevel()
      top.title(title)

      frameAbout = Frame(top)
      frameAbout.pack(fill=BOTH,expand="YES", padx=20, pady=25)
      Label(frameAbout, font=("Helvetica",13, "bold"),text="Aplikasi Pengolahan Data Produk (APDAPRO)", anchor="w", justify=LEFT).pack()
      Label(frameAbout, text="Program untuk mengelola data produk yang\nada di sebuah toko sederhana. Dibuat untuk memenuhi\ntugas praktikum dpbo ke3", font=("Helvetica", 11), justify=LEFT).pack()
      Label(frameAbout, text="Developed By Fajar Zuliansyah Trihutama", font=("Helvetica", 11, 'italic'), justify=LEFT).pack(side=LEFT)

   # proses isi data ke list of object
   def process(self, nama, hJual, hBeli, jenis, kondisi, item1,item2):
      if(not nama.get() or not jenis.get() or not hJual.get() or not hBeli.get()):
         messagebox.showinfo("Warning", "Tidak boleh ada data yang kosong")
      else:   
         tbh = []
         if item1 != "N":
            tbh.append(item1)
         if item2 != "N":
            tbh.append(item2)
         # messagebox.showinfo('Debug', nama.get() + jenis.get() + hJual.get() + hBeli.get() + kondisi.get() + item1.get()+item2.get() + self.win.filename)
         try:
            self.data.append(Produk(nama.get(),hBeli.get(),hJual.get(),jenis.get(),kondisi.get(),tbh,self.win.filename))
            messagebox.showinfo("Sukses", "Data anda sudah berhasil ditambahkan")
            nama.delete(0, 'end')
            hJual.delete(0, 'end')
            hBeli.delete(0, 'end')
         except:
            messagebox.showinfo("Warning", "Tidak boleh ada data yang kosong")
   
   # tampil data yang ada dengan window baru
   def allSubmissions(self, title):
      if self.data:
         top = Toplevel()
         top.title(title)

         all_frame = LabelFrame(top, text="Data Submissions", padx=10, pady=10)
         all_frame.pack(padx=10, pady=10)

         # table header
         header = Label(all_frame, text="No")
         header.grid(row=0, column=0)

         header = Label(all_frame, text="Jenis")
         header.grid(row=0, column=1)

         header = Label(all_frame, text="Nama")
         header.grid(row=0, column=2)

         header = Label(all_frame, text="Kondisi")
         header.grid(row=0, column=3)

         # table row data 
         for index, pro in enumerate(self.data):

            idx = Label(all_frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
            idx.grid(row=index+1, column=0)

            jenis = Label(all_frame, text=pro.getjenis(), width=15, borderwidth=1, relief="solid")
            jenis.grid(row=index+1, column=1)
            
            name = Label(all_frame, text=" " + pro.getnama(), width=30, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index+1, column=2)

            kondisi = Label(all_frame, text=" " + "Baru" if pro.getkondisi() else "Bekas", width=10, borderwidth=1, relief="solid", anchor="w")
            kondisi.grid(row=index+1, column=3)

            detail = Button(all_frame, text="Details ", command=lambda index=index: self.details(index))
            detail.grid(row=index+1, column=4)
      else:
         messagebox.showinfo("Empty", "Data Submissions Kosong")

   # hapus semua data
   def clearSubmissions(self):
      self.data.clear()

   # atur layouting/ui
   def set_widget(self):
      # mainframe
      main_frame = Frame(self.win)
      main_frame.pack(fill=BOTH, expand="YES")

      # info at bottom
      self.info_develop = Label(main_frame, text="Tugas Praktikum DPBO Ke-3", relief=SUNKEN, bd=1, pady=7)
      self.info_develop.pack(side=BOTTOM, fill=X)


      # left frame
      frame_kiri = Frame(main_frame, bd=5, relief=GROOVE)
      frame_kiri.pack(fill=BOTH, expand=YES, side=LEFT, padx=(35,5), pady=(50,50))

      # isi frame kiri
      Label(frame_kiri, text="Nama").grid(row=3, column=3, padx=15, pady=10, sticky=W)

      nama = Entry(frame_kiri, width=28)
      nama.grid(row=3, column=4)

      Label(frame_kiri, text="Harga Beli").grid(row=4, column=3, padx=15, pady=10, sticky=W)

      harga_beli = Entry(frame_kiri, width=28)
      harga_beli.grid(row=4, column=4)

      Label(frame_kiri, text="Harga Jual").grid(row=5, column=3, padx=15, pady=10, sticky=W)

      harga_jual = Entry(frame_kiri, width=28)
      harga_jual.grid(row=5, column=4)

      # DROPDOWN
      Label(frame_kiri, text="Jenis").grid(row=6, column=3, padx=15, pady=10, sticky=W)

      options = ["Komputer", "Handphone", "Aksesoris", "Elektronik"]

      self.clicked = StringVar()
      self.clicked.set(options[0])

      drop = OptionMenu(frame_kiri, self.clicked, *options)
      drop.grid(row=6, column=4, sticky=W)

      # RADIOBUTTON
      kondisi = [
         ("Baru", 1),
         ("Bekas", 0)
      ]

      radioB = []
      kondisiLb = Label(frame_kiri,text="Kondisi").grid(row=7, column=3, padx=15, pady=10, sticky=W)
      selected = StringVar()
      selected.set(1)
      i = 7

      for text, condition, in kondisi:
         radioB.append(Radiobutton(frame_kiri, text=text, variable=selected, value=condition).grid(padx=1, pady=0, sticky=W, row=i, column=4))
         i+=1

      # CHECKBOX
      fiturLb = Label(frame_kiri,text="Tambahan").grid(row=9, column=3, padx=15, pady=10, sticky=W)
      item1 = StringVar()
      c1 = Checkbutton(frame_kiri, text="Bervariasi", variable=item1, onvalue='Bervariasi', offvalue='N')
      c1.deselect()
      c1.grid(row=9,column=4, sticky=W)

      item2 = StringVar()
      c2 = Checkbutton(frame_kiri, text="Grosir", variable=item2, onvalue="Grosir", offvalue="N")
      c2.deselect()
      c2.grid(row=10, column=4, sticky=W)

      # OPENFILE PHOTO
      openfile_btn = Button(frame_kiri, text="OPEN PHOTO FILE", relief=GROOVE, command=lambda frame=frame_kiri: self.openFile(frame)).grid(row=11, column=3, columnspan=2, padx=(17, 0), sticky=EW, pady=(15, 5))

      # SUBMIT BUTTON
      b_add = Button(frame_kiri, text="SUBMIT", command=lambda nama=nama, hJual=harga_jual, hBeli=harga_beli,jenis=self.clicked, kondisi=selected, item1=item1, item2=item2:self.process(nama, hJual, hBeli, jenis, kondisi, item1,item2), relief=GROOVE)
      b_add.grid(row=13, column=3, columnspan=3, sticky=EW, pady=(0,20), padx=(17,0))


      # right frame
      frame_kanan = Frame(main_frame, bd=5)
      frame_kanan.pack(fill=BOTH, expand=YES, side=LEFT, padx=10, pady=40)

      # isi frame kanan
      judul_app = Label(frame_kanan, text="Aplikasi Pengolahan \nData Produk", fg="blue", font=("Helvetica", 30), justify=LEFT)
      judul_app.pack(side=TOP, pady=(45, 5))

      desc_app = Label(frame_kanan, text="Program untuk mengelola data produk yang\nada di sebuah toko sederhana. Dibuat untuk memenuhi\ntugas praktikum dpbo ke3", font=("Helvetica", 12), justify=LEFT)
      desc_app.pack(side=TOP, fill=X, padx=(10, 0))

      submission_btn = Button(frame_kanan,bg='DeepSkyBlue2',activebackground='dodgerblue', activeforeground='white', font=('Helvetica', 11, 'bold'), text="SEE ALL SUBMISSIONS", command=lambda title="All Submission":self.allSubmissions(title),relief=GROOVE)
      submission_btn.pack(fill=X, padx=(30,0), pady=(20,5))

      clear_submission_btn = Button(frame_kanan, bg='red3', fg='white', activebackground='red2', activeforeground='white', font=('Helvetica', 11, 'bold'), text="CLEAR SUBMISSION", command=self.clearSubmissions,relief=GROOVE)
      clear_submission_btn.pack(fill=X, padx=(30, 0), pady=(0, 5))

      about_btn = Button(frame_kanan, font=('Helvetica', 11, 'bold'), text="ABOUT", command=lambda title='About': self.openAbout(title),relief=GROOVE)
      about_btn.pack(fill=X, padx=(30, 0), pady=(0, 20))

      exit_btn = Button(frame_kanan, bg='gray23', fg='white',font=('Helvetica', 11, 'bold'), text="EXIT", command=self.onClose,relief=GROOVE)
      exit_btn.pack(side=BOTTOM, fill=X, padx=(30, 0), pady=(0, 15))



