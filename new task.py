import random
#def task1():
#    list1 = []
#    list2 = []
#    num1 = random.randint(1, 20)
#    list.append(num1)
#    for i in range(5):
#        num2 = random.randint(1,20)
#        list1.append(num2)
#    for i in list1:
#        if i % 3 == 0:
#            list2.append(i)
#    print(list1)
#    print(list2)
#task1()


def task2():
    def writeUser():
        with open(names.txt, "w") as new_file :
            while True:
                name = input("введите имя")
                if name =='stop':
                    break
                new_file.write(name + '\n')


    def readUsers():
        list1 = []
        with open("names.txt", "r") as new_file:
            list = new_faile.redlines()
            for i in list1:
                if i[0] != 'A':
                    print(i)
    print("выюерите действие")
    print("1. Добавить пользователей")
    print("2. Посмотреть пользователей")
    action= int(input("введите действие"))
    if action == 1:
        writeUser()
    elif action == 2:
        readUsers()
    else:
        print('error')