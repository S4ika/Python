import math


# Увеличиваем цену на 15 %
def profit(dictionary):
    for key in dictionary:
        dictionary[key] = math.ceil(dictionary[key] * 1.15)


# Корректируем цену так, чтобы она оканчивалась на 5 или 0
def beauty_price(dictionary):
    for key in dictionary:
        last_digit = dictionary[key] % 10  # Взяли последнюю цифру
        if last_digit % 5 > 2:  # Проверка на округление в большую сторону
            dictionary[key] += 5 - last_digit % 5
        else:
            dictionary[key] -= last_digit % 5


# prices = {'Apple':800, 'Banana': 600, 'Milk': 700}
prices = {}
while True:
    print("Введите товар: ")
    key = input()
    print("Введите цену:")
    prices[key] = int(input())
    print("Ввести еще?\n0.Нет\n1.Yes")
    check = int(input())
    if check == 0:
        break

profit(prices)
beauty_price(prices)
print(prices)