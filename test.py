#!/usr/bin/env python
"""Hello World, fizbuzz and 99bottlesofbeer"""
print ("Hello World!\n")




for i in range(1,99):
    if not i%15:
        print("fizzbuzz")
    elif not i%3:
        print("fizz")
    elif not i%5:
        print("buzz")
    else:
        print(i)


print ("\n99 bottles of beer")
for i in range(0,99)[::-1]:
    if i<1:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall...")
    else:
        print(i, " bottles of beer on the wall, ", i ," bottles of beer")
        i-= 1
        print("Take one down, pass it around, " , i , " bottles of beer on the wall")
