# Casing methods: capitalize, lower, upper, title, swapcase, casefold, istitle, isupper, islower.

examples = [
    "hello world", 
    "PYTHON Programming", 
    "ßharp", 
    "This Is Title"
]

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
