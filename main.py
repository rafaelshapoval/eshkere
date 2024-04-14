
def task1():
    numbers.txt = []
    with open("numbers.txt") as file1:
        for line in file1:
            numbers.append([float(x) for x in line.split()])




def task5():
 num1 = int(input("введите название любымих фильмов"))
move = int(input("что бы закончить напишите "))






def task6():




while true:
    print("выберете действие:")
    print("1. добавить новую задачу")
    print("2. просмотеть список задач")
    print("3. отметить задачу как выполненную")
    print("4. удалить задачу")
    print("5. выйти из программы")

choice = input("введите номер действия: ")

    if choice == "1"
            create_task_list()
    elif choice == "2"
        view_task_list()
    elif choice == "3"
        mark_task_done()
    elif choice == "4"
        delete_task()
    elif choice == "5"
        break
   else:
    print("неккоректный ввод.Попробуйте снова.")











#   def create_task_list():
#       task = []
#       with open("tasks.txt", "r") as file:
#           tasks = file.readlinse()
#
#
#       print("список задач:")
#       for i, task enemerete(tasks)
#   print(f"{i + 1}. {task.strip()}")


#ask_num = int(input("введите номер задачи для удаления:"))


#ef task1():
#   a1 = int(input("введите первое число"))
#   a2 = int(input("введите второе число"))
#   randomnum1 = random.randint(a1,a2)
#   print("num = ", randomnum1)
#   list('список')
#   ['', '', '', '', '', '','']







#    even_list = list()
#    not_even_list = list()
#    while True:
#        number = int(input("введите число: "))
#        if numbers ==0:
#            break
#        if numbers % 2 == 0:
#            even_list.append(numbers)
#    print(even_list)
#    print(not_even_list)



#print('Как тебя зовут, воин?')
#name = input()
#print(f'Добро пожаловать в земли Неверленда, {name}')
#print('Выбери свою сильную черту')
#print('1. Ловкость')
#print('2. Сила')
#print('3. Живучесть')
#ch = int(input())
#while ch != 1 and ch != 2 and ch != 3:
#    print('Некорректный ввод. Выбери заново.')
#    ch = int(input())
#if ch == 1:
#    speed = 10
#    power = 5
#    hp = 50
#elif ch == 2:
#    speed = 5
#    power = 10
#    hp = 50
#else:
#    speed = 5
#    power = 5
#    hp = 100
#
#coins = 30
#max_hp = hp
#
#locations = {
#    0: ('Торговый переулок', (1, 2)),
#    1: ('Катакомбы', (3, 0)),
#    2: ('Центральная площадь', (0,)),
#    3: ('Подземелье', (1,))
#}
#
#enemies = {
#    0: ('Воришка', (12, 4, 20)),
#    1: ('Крыса-мутант', (5, 20, 100)),
#    2: ('Пьянчуга', (6, 6, 30)),
#    3: ('Бешеный гоблин', (15, 15, 95))
#}
#
#shop = {
#    0: ('Зелье регенерации', 'Восстанавливает часть здоровья', 10),
#    1: ('Ржавый меч', 'Толку от него не много, но  лучше, чем голые кулаки', 5),
#    2: ('Боевой топор', 'Удобное оружие, быстрое и эффективное', 20),
#    3: ('Двуручный меч', 'Наносит противнику большой урон, но требует мастерства', 20)
#}
#
#weapons = {
#    'Ржавый меч': (1.2, 1),
#    'Боевой топор': (1.5, 2),
#    'Двуручный меч': (2.5, 0.5)
#}
#
#current_location = 0
#end_game = False
#weapon = None
#elixir_count = 0
#
#while not end_game:
#    if current_location == 0:
#        variant_number = 1
#        variants_count = 1 + len(locations[0][1])
#        print('Ты гуляешь по торговой площади среди прилавков.')
#        print(f'{variant_number}. Подойти к торговцу')
#        variant_number += 1
#        for i in locations[0][1]:
#            print(f'{variant_number}. {locations[i][0]}')
#            variant_number += 1
#        print('Выбери действие')
#        choice = int(input())
#        while choice <= 0 or choice > variants_count:
#            print('Некорректный вариант. Выбери действие')
#            choice = int(input())
#
#        if choice == 1:
#            leave = False
#            while not leave:
#                print(f"У тебя есть {coins} монет")
#                print("Товары:")
#                for product in shop:
#                    print(f'{product}: {shop[product][0]}')
#                print(f'{len(shop)} Выйти из магазина')
#                print('Выбери действие')
#                shop_choice = int(input())
#                while shop_choice < 0 or shop_choice > len(shop):
#                    print('Некорректный вариант. Выбери действие')
#                    shop_choice = int(input())
#
#                if shop_choice == len(shop):
#                    leave = True
#                else:
#                    print(shop[shop_choice][0])
#                    print(shop[shop_choice][1])
#                    print(f'Цена: {shop[shop_choice][2]} монет')
#                    print(f"1. Купить {shop[shop_choice][0]}")
#                    print("2. Вернуться назад")
#                    choice = int(input())
#                    while choice != 1 and choice != 2:
#                        print('Некорректный выбор')
#                        choice = int(input())
#                    if choice == 1:
#                        if coins >= shop[shop_choice][2]:
#                            coins -= shop[shop_choice][2]
#                            if shop_choice == 0:
#                                elixir_count += 1
#                            else:
#                                weapon = shop[shop_choice][0]
#                        else:
#                            print("У вас не достаточно монет")
#                    else:
#                        continue



























