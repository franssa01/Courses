"""
Make a code that read a whole number and ask to user choose which will be the base of
conversion :
1 - Binary
2 - Octal
3 - Hexadecimal
"""

# number = int(input("Type a whole number: "))
# print("""Choose one of the conversion bases:
# [ 1 ] Convert to Binary
# [ 2 ] Convert to Octal
# [ 3 ] Convert to Hexadecimal
# """)
# conversion = int(input("Your option: "))
#
# if conversion == 1:
#     print("{} converted to Binary is {}".format(number, bin(number)[2:]))
# elif conversion == 2:
#     print("{} converted to Octal is {}".format(number, oct(number)[2:]))
# elif conversion == 3:
#     print("{} converted to Hexadecimal is {}".format(number, hex(number)[2:]))
# else:
#     print("Invalid option")


# Or


def converter(num=0, binary=False, octal=False, thexadecimal=False, hexadecimal=False):
    if binary:
        print(f"{num} Convert to Binary is → {num:b}")
    if octal:
        print(f"{num} Convert to Octal is → {num:o}")
    if thexadecimal:
        print(f"{num} Convert to Tiny Hexadecimal is → {num:x}")
    if hexadecimal:
        print(f"{num} Convert to Hexadecimal is → {num:X}")
    else:
        print("Please, choose some type of conversion")


converter(5)