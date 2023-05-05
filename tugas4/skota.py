class Nama_Kota:
    def __init__(self, name):
        self.name = name
class Bahasa:
    def __init__(self, bahasa):
        self.bahasa = bahasa
class Negara:
    def __init__(self, nama_kota, bahasa):
        self.nama_kota = nama_kota
        self.bahasa = bahasa

nama_kota1 = Nama_Kota("cirebon")
nama_kota2 = Nama_Kota("Bandung")
nama_kota3 = Nama_Kota("Madura")
nama_kota4 = Nama_Kota("Depok")
bahasa = Bahasa("Bahasa Indonesia")

negeri = Negara([nama_kota1, nama_kota2, nama_kota3, nama_kota4], bahasa)
print(negeri.nama_kota[0].name)
