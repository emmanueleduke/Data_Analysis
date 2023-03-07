#!/usr/bin/python3
for i in range(0, 10):
    for o in range(1, 10):
        if i >= o:
            continue
        elif i == 8 and o == 9:
            print("{} {} ".format(i, o))
        else:
            print("{} {} ".format(i, o), end=", ")
