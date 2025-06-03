for i in range(1, 101):
    if a % 10 == 1:
        print(i, "манул")
    elif (i >= 2 and i <= 4) or i == 22:
        print(i, "манула")
    else:
        print(i, "манулов")