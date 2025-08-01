string = "Data Structures and Algorithms"


# Indexing and slicing 

print("\n\n---- Indexing and Slicing ----\n\n")
print(string[8]) # u
print(string[-1]) # s (negative indexing)

print(string[0:4])  # Data
print(string[5:15])  # Structures

print(string[:]) # Data Structures and Algorithms
print(string[:15]) # Data Structures
print(string[16:]) # and Algorithms

print(string[::2]) # Dt tutrsadAgrtm (every second character from the string)
print(string[5:15:3]) # Suus


print(string[::-1]) # smhtiroglA dna serutcurtS ataD     (shortcut to reverse the string)
print(string[29::-1]) # smhtiroglA dna serutcurtS ataD (reversing the entire string)


print(string[0:28:-1]) # (empty string, as the step is negative and the start index is less than the end index)
print(string[29:0:-1]) # smhtiroglA dna serutcurtS ata
print(string[-1::]) # s
print(string[-1:]) #s 
print(string[:-1]) # Data Structures and Algorithm (excluding the last character)








# String Concatenation and Repetition

a = "Hello"
b = "Python"


print("\n\n---- String Concatenation and Repetition ----\n\n")

print(a + " " + b)  # Hello Python
print(f"{a} {b}")  # Hello Python (using f-string for formatting)
print("{} {}".format(a, b))  # Hello Python (using format method)


print(a * 3)  # HelloHelloHello (repeating the string three times)
print((a + " ") * 3)  # Hello Hello Hello (repeating with a space in between)






# String Membership 

# in keyword checks if a substring exists within a string
# not in keyword checks if a substring does not exist within a string

# both in and not in operators return a boolean value (True or False)

print("\n\n---- String Membership ----\n\n")
print("Data" in string)  # True (substring check)
print("data" in string)  # False (case-sensitive check)
print("Data" not in string)  # False (substring check)
print("Python" in string)  # False (substring check)
print("Structures" in string)  # True (substring check)


