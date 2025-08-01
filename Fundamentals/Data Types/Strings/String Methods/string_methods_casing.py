# Casing methods: capitalize, lower, upper, title, swapcase, casefold, istitle, isupper, islower.

examples = ["hello world", "PYTHON Programming", "ßharp", "This Is Title"]

for text in examples:
    print(f"Original: {text}")
    print(" capitalize():", text.capitalize())
    print(" lower():   ", text.lower())
    print(" upper():   ", text.upper())
    print(" swapcase():", text.swapcase())
    print(" title():   ", text.title())
    print(" casefold():", text.casefold())
    print(" islower(): ", text.islower())
    print(" isupper(): ", text.isupper())
    print(" istitle(): ", text.istitle())
    print("-" * 40)


"""# Output:

Original: hello world
 capitalize(): Hello world
 lower():    hello world
 upper():    HELLO WORLD
 swapcase(): HELLO WORLD
 title():    Hello World
 casefold(): hello world
 islower():  True
 isupper():  False
 istitle():  False
----------------------------------------
Original: PYTHON Programming
 capitalize(): Python programming
 lower():    python programming
 upper():    PYTHON PROGRAMMING
 swapcase(): python pROGRAMMING
 title():    Python Programming
 casefold(): python programming
 islower():  False
 isupper():  False
 istitle():  False
----------------------------------------
Original: �harp
 capitalize(): Ssharp
 lower():    �harp
 upper():    SSHARP
 swapcase(): SSHARP
 title():    Ssharp
 casefold(): ssharp
 islower():  True
 isupper():  False
 istitle():  False
----------------------------------------
Original: This Is Title
 capitalize(): This is title
 lower():    this is title
 upper():    THIS IS TITLE
 swapcase(): tHIS iS tITLE
 title():    This Is Title
 casefold(): this is title
 islower():  False
 isupper():  False
 istitle():  True
----------------------------------------

"""
