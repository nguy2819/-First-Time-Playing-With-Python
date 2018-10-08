# Write out "Hello World"
print("Hello World")

# Drawing a Shape
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# Variables & Data Types

character_name = "George"
character_age = "70"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")

# Also we can change in the character_name from this second part down
character_name = "Mike"
print("He is really like the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

# Result will be:
# There once was a man named George,
# he was 70 years old.
# He is really like the name George,
# but didn't like being 70.

# Working With Strings
print("Tien Borland")
print("Tien\nBorland") #2 lines
print("Tien\"Borland") #print a " in the middle
print("Tien\Borland") #print a \ in the middle

phrase = "David Borland"
print(phrase + " is a wonderful person")
print(phrase.upper()) # DAVID BORLAND
print(phrase.lower()) # david borland
print(phrase.isupper()) # boolean question? => Answer is False
print(phrase.upper().isupper()) # changed to all uppercase - then as if it is uppercase or not => Answer is True
print(len(phrase)) # 13
print(phrase[0]) # D
print(phrase.index("a")) # 1
print(phrase.replace("David", "Eliana")) # Eliana Borland