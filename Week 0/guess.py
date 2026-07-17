<<<<<<< HEAD
def get_guess():
    guess = int(input("Guess a number between 1 and 10: "))
    return guess

def main():
    guess = get_guess()
    while guess != 5:
        print("Wrong!")
        guess = get_guess()
    else:
        print("Correct!")
main()

'''
The while loop continues as long as guess is not 5.
When guess becomes 5, the condition
    guess != 5
evaluates to False, so Python exits the loop and
continues to the next line after the loop.
Because of this, print("Correct!") only runs after
the user has entered 5.

def main():
    guess = get_guess()
    while guess != 5:
        print("Wrong!")
        guess = get_guess()

print("Correct!")
main()
'''
=======
def get_guess():
    guess = int(input("Guess a number between 1 and 10: "))
    return guess

def main():
    guess = get_guess()
    while guess != 5:
        print("Wrong!")
        guess = get_guess()
    else:
        print("Correct!")
main()

'''
The while loop continues as long as guess is not 5.
When guess becomes 5, the condition
    guess != 5
evaluates to False, so Python exits the loop and
continues to the next line after the loop.
Because of this, print("Correct!") only runs after
the user has entered 5.

def main():
    guess = get_guess()
    while guess != 5:
        print("Wrong!")
        guess = get_guess()

print("Correct!")
main()
'''
>>>>>>> 14e4d9d30ed097a8baaec6dfd8a5fe660416ffdc
