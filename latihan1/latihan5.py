class PesawatTerbang:
 
 def __init__(self, maskapai, tujuan):
    self.maskapai = maskapai
    self.tujuan = tujuan

 def info(self):
    print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}")
pesawatA = PesawatTerbang("Lion Air", "Jakarta - Lampung")
pesawatA.info()

#Dalam hal ini mobilA, mahasiswaB, lingkaranA, bukuA, dan pesawatA adalah objek
