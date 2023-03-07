#!/usr/bin/python3
for em in range(0, 100):
    if em == 99:
        print("{}".format(em))
    else:
        print("{:02}".format(em), end=", ")
