def hello(to):
    print("Hello,", to)

name = input("What's your name? ").strip().title()
first, last = name.split(" ")
hello(name)