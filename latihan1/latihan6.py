class Kalkulator:
 @staticmethod
 def add(x, y): 
    return x + y

 @staticmethod
 def subtract(x, y):
    return x - y

 @staticmethod
 def multiply(x, y):
    return x * y
 @staticmethod
 def divide(x, y):
    if y == 0:

        raise ValueError('Tidak dapat membagi dengan nol.')
    return x / y

# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(3, 5)) # Output: 8
print(Kalkulator.subtract(10, 7)) # Output: 3

# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(4, 6)) # Output: 24
print(Kalkulator.divide(12, 4)) # Output: 3.0