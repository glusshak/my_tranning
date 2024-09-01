
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
a = 0
running = True
while running:
    if(my_list[i] == 0):
        i += 1
        continue
    elif (a < my_list[i]):
        print(my_list[i])
    else:
        running = False
    i += 1



