def greet(input):
    if "hello" in input:
        return "Hello, there"
    else:
        return "I don't understand"
    

greeting = greet("hello, computer")
print(greeting)