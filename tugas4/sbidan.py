class Bidan:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        
class Puskesmas:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def daftar_doctor(self):
        for position in self.position:
            print(position.name, position.department)
bidan1 = Bidan("saritem", "Heart and Liver")
bidan2 = Bidan("Sulisti", "Incomplicated")
hospital = Puskesmas("SEDULURAN", [bidan1, bidan2])
hospital.daftar_doctor()
