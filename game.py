from random import *
a = randint(1, 10)
lives = 3
while lives > 0:
    print("Осталось жизней", lives)
    print("Какое число загадано?")
    ua = int(input())
    if ua < 1 or ua > 10:
        print("Число должно быть от 1 до 10 включительно")
    elif ua == a:
        print("Победа")
        break
    elif a > ua:
        print("Загаданное число больше")
    else:
        print("загаданное число меньше")
    lives -= 1
print("Было загадано чисто:", a)
