class membership:
    diskon = 0.1
    def __init__(self,nama,kode,treat,harga):
        self.nama = nama
        self.kode = kode
        self.treat = treat
        self.harga = harga

    def display(self):
        print('\n\tDiskon Membership\t\n','='*30)
        print('Nama\t\t: ',self.nama)
        print('Kode Member\t: ',self.kode)
        print('Treatment\t: ',self.treat)
        print(f'Bayar\t\t:  {self.harga}\n')

    def bayar(self):
        diskon = (self.harga)*self.diskon
        self.harga = self.harga-diskon
        return self.harga

class platinum(membership):
    diskon = 0.2
    def __init__(self,nama,kode,treat,harga):
        super().__init__(nama,kode,treat,harga)
        
    def bayar(self):
        diskon = (self.harga)*self.diskon
        self.harga = self.harga-diskon
        return self.harga

class gold(membership):
    diskon = 0.45
    def __init__(self,nama,kode,treat,harga):
        super().__init__(nama,kode,treat,harga)
        
    def bayar(self):
        diskon = (self.harga)*self.diskon
        self.harga = self.harga-diskon
        return self.harga

member1 = membership('Risti','D230329','Spa',280000)
member1.bayar()
member1.display()

member2 = gold('ACIP','A210112','Facial Treatment',650000)
member2.bayar()
member2.display()

member3 = platinum('Lutfi','A201031','Facial Treatment',600000)
member3.bayar()
member3.display()