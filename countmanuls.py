for i in range(1, 101):
    if i >= 11 and i <= 14:
        print(i, "манулов")
    elif i % 10 == 1:
        print(i, "манул")
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print(i, "манула")
    else:
        print(i, "манулов")
