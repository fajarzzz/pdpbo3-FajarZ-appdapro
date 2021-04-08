class Produk:
   def __init__(self, nama, hBeli, hJual, jenis, kondisi, tambahan, picture):
      self.nama = nama
      self.hBeli = hBeli
      self.hJual = hJual
      self.jenis = jenis
      self.kondisi = kondisi
      self.tambahan = tambahan
      self.picture = picture

   # GETTER
   def getnama(self):
      return self.nama
   
   def gethBeli(self):
      return self.hBeli

   def gethJual(self):
      return self.hJual

   def getjenis(self):
      return self.jenis

   def getkondisi(self):
      return self.kondisi

   def gettambahan(self):
      return self.tambahan

   def getpicture(self):
      return self.picture

   # SETTER
   def setnama(self, nama):
      self.nama = nama
   
   def sethBeli(self, hBeli):
      self.hBeli = hBeli

   def sethJual(self, hJual):
      self.hJual = hJual

   def setjenis(self, jenis):
      self.jenis = jenis

   def setkondisi(self, kondisi):
      self.kondisi = kondisi

   def settambahan(self, tambahan):
      self.tambahan = tambahan

   def setpicture(self, picture):
      self.picture = picture