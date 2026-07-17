<<<<<<< HEAD
# Ask user for their name then remove whitespace and capitalize it
name = input("What is your name? ").strip().title()

#Split user's name into first and last names
first, last = name.split(" ")
# Say hello to user
=======
# Ask user for their name then remove whitespace and capitalize it
name = input("What is your name? ").strip().title()

#Split user's name into first and last names
first, last = name.split(" ")
# Say hello to user
>>>>>>> 14e4d9d30ed097a8baaec6dfd8a5fe660416ffdc
print(f"Hello, {last}")