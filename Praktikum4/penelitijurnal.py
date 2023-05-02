class Jurnal:
    def __init__(self,title,date):
        self.title = title
        self.date = date

class peneliti:
    def __init__(self,nama,jurnal):
        self.nama = nama
        self.jurnal = jurnal

    def daftar_jurnal(self):
        print(f'\nPeneliti\t:  {self.nama}\n')
        for jurnal in self.jurnal:
            print(f'Judul\t\t: ',jurnal.title)
            print(f'Published\t:  {jurnal.date}')
           
jurnal1 = Jurnal('The Paradox of Indonesian Digital Economy Development', 2020)
jurnal2 = Jurnal('Towards Data Sovereignty in Cyberspace', 2015)
peneliti1 = peneliti('AS Sastrosubroto', [jurnal1, jurnal2])
jurnal3 = Jurnal('A Century of Trends in Adult Human Height', 2016)
jurnal4 = Jurnal('Repositioning of The Global Epicentre of Non-optimal Cholesterol', 2020)
peneliti2 = peneliti('IS Widyahening', [jurnal3, jurnal4])
peneliti1.daftar_jurnal()
peneliti2.daftar_jurnal()