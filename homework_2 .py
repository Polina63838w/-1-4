#2 задача
#def summa(a, b):
#    if a == 0:
#        return b;
 #   return summa(a-1, b+1)

#1 задача
def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))
base = int(input("Введите число: "))
exp = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(base, exp))