def some_decorator(func):
    def wrapper(*args):
        print("Before func is called... we do some stuff here...")
        func(*args)
        print("After func is called... we do some stuff here...")

    return wrapper


@some_decorator
def greet(greeting: str):
    print(f"This is my greeting: {greeting}")


greet("Heeeyy!")
