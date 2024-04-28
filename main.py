print("Какой формы апельсин")
otvet = input()
score = 0
if otvet == "круг":
    score += 1

print("какого цвета яблоко?")
otvet = input()
score = 1
if otvet == "красный":
    score += 2

print("2 + 2?")
otvet = input()
score = 2
if otvet == 4:
    score += 3

print("Хотите ли вы себе Lamborgini?")
otvet = input()
score = 3
if otvet == "Да":
    score += 4

print("Хотите ли вы себе бизнес с такими деньгами?")
otvet = input()
score = 4
if otvet == "Частично":
    score += 5

print("Пойдете ли вы играть в казино?")
otvet = input()
score = 5
if score == "ДА, ВЕДЬ Я МЕЛСТРОЙ":
    score += 6

print(score)