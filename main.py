
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






























