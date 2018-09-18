#! /usr/bin/env python3
# conditional.py

x = 4
y = 6

qt = (x != y) # >, <, == , <=, >=, !=
print(qt)

# boolean
my_bool = True
print(my_bool)

# Conditional
if (x < y):
    print("Less than")
elif (x == y):
    print("Equal to")
else:
    print("Greater than")