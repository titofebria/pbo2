class kerja_fulltime:
    def __init__(self,nama,jabatan,jam_kerja,gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.jam_kerja = jam_kerja
        self.gaji = gaji

    def bonus(self):
        return self.gaji*0.15

    def display(self):
        print('\n\t\tInfo Pegawai\t\t\n'+'='*40)
        print('Nama\t\t: ',self.nama)
        print('Jabatan\t\t: ',self.jabatan)
        print(f'Jam Kerja\t:  {self.jam_kerja} jam')
        print('Gaji\t\t: ',self.gaji)

class kerja_partime(kerja_fulltime):
    def __init__(self,nama,jabatan,jam_kerja,gaji):
        super().__init__(nama,jabatan,jam_kerja,gaji)

    def bonus(self):
        return self.gaji*0.05

def info_bonus(object):
    x = object.bonus()
    y = object.gaji + object.bonus()
    print(f'Bonus\t\t:  {x}')
    print(f'Total Gaji\t:  {y}\n')


worker1 = kerja_fulltime('Tito','Senior Data Scientist',5,7500000)
worker1.display()
info_bonus(worker1)

worker2 = kerja_fulltime('Angga','Designer',6,4500000)
worker2.display()
info_bonus(worker2)
