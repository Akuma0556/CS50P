# Ask user for their name then remove whitespace and capitalize it
name = input("What is your name? ").strip().title()

#Split user's name into first and last names
first, last = name.split(" ")
# Say hello to user
print(f"Hello, {last}")