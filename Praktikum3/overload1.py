class jajan:
    def __init__(self, fare):
        self.fare = fare

    def __add__(self, other):
        return self.fare+other.fare

eskelapa = jajan(10)
baso = jajan(13)
total = eskelapa+baso
print(f'\nHarga Total: {str(total)}k\n')