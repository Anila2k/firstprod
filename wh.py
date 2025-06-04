q = "Какой сегодня месяц?"
ra = "июнь"
print(q)
ua = input()
c = 0
while ua != ra:
    print("Wrong! Try again")
    ua = input()
    c += 1
print("Well done!")
print("Ты сказал правильно с", c, "раза")

from random import *
a = randint(1, 10)
print(a)
