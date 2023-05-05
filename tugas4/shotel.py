class Rumah:
    def __init__(self, area):
        self.area = area

class Hotel:
    def __init__(self, area):
        self.area = area

class Bangunan:
    def __init__(self, rumah, hotel):
        self.rumah = rumah
        self.hotel = hotel

rumah = Rumah("65 m")
hotel = Hotel("130 m")
bangunan = Bangunan(rumah, hotel)
print(bangunan.rumah.area) 
print(bangunan.hotel.area)
