import math

def calculate(x, y, z):
    if y <= 0:
        return "Логарифмічна помилка, значення логарифма менше 0"
    if math.atan(x)+math.atan(z) == 0:
        return "Помилка, ділення на 0"

    return pow((pow(x, 6) + pow(math.log(y), 2)), 1/3) + (math.exp(math.fabs(x-y))*pow(math.fabs(x-y), x+y))/(math.atan(x)+math.atan(z))


def main():
    # x = -2.235 * 0.01
    # y = 2.23
    # z = 15.221

    print("Тут-ту-ру")
    x = float(input("Введіть значення х: "))
    y = float(input("Введіть значення y: "))
    z = float(input("Введіть значення z: "))
    func = calculate(x, y, z)
    print("")
    return ("Результат програми: ", func)


print(main())




