cp = 0
print("1 как меня зовут?")
np = 5
for i in range(5):
    np -= 1
    b = input()
    if b == "Алина":
        print("верно")
        cp += 1
        print("твои баллы:", cp)
        break
    else:
        print("попробуй еще раз", "у тебя осталось", np, "попытки(а)")
print("2 какой мой любимый цвет?")
np = 5
for i in range(5):
    np -= 1
    a = input()
    if a == "фиолетовый":
        print("верно")
        cp += 1
        print("твои баллы:", cp)
        break
    else:
        print("попробуй еще раз", "у тебя осталось", np, "попытки(а, ок)")
print("3 в какой класс я перехожу?")
np = 5
for i in range(5):
    np -= 1
    a = int(input())
    if a == 9:
        print("верно")
        cp += 1
        print("твои баллы:", cp)
        break
    else:
        print("попробуй еще раз", "у тебя осталось", np, "попытки(а)")
