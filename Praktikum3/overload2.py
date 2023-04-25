class vektor:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'{self.x}i{self.y:+}j'

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


vektor1 = vektor(9,12)
print('\nVektor\t\t: '+str(vektor1))
print('Panjang Vektor\t: ',abs(vektor1),'\n')