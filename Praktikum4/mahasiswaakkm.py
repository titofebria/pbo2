class mahasiswa_kkm:
    def __init__(self,mahasiswa=None):
        if mahasiswa is None:
            self.mahasiswa = []
        else:
            self.mahasiswa = mahasiswa

    def add_mahasiswa(self,mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        for mhs in self.mahasiswa:
            print(f'Nama\t\t: ',mhs.nama)
            print(f'Jurusan\t\t: ',mhs.jurusan)
            print(f'Semester\t: ',mhs.semester)

class Mhs:
    def __init__(self,nama,jurusan,semester):
        self.nama = nama
        self.jurusan = jurusan
        self.semester = semester

    def get_nama(self):
        return self.nama

    def get_jurusan(self):
        return self.jurusan
    
    def get_semester(self):
        return self.semester

class kkm:
    def __init__(self,name_kkm,mahasiswa_kkm):
        self.name_kkm = name_kkm
        self.mahasiswa_kkm = mahasiswa_kkm

    def tampil(self):
        print(f'\nTempat KKM\t: {self.name_kkm}\n')

mhs1 = Mhs('titofebrianggara', 'Teknik Informatika', 4)
mhs2 = Mhs('maolana', 'Teknik Informatika', 4)
mhs3 = Mhs('alimabrur', 'Teknik Informatika', 4)
mhs_kkm = mahasiswa_kkm([mhs1, mhs2, mhs3])
Kkm = kkm('Busan, South Korea', mhs_kkm)
Kkm.mahasiswa_kkm.mahasiswa
Kkm.tampil()
Kkm.mahasiswa_kkm.daftar_mahasiswa()