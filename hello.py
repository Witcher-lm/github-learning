# My first Python program on GitHub

def greet(name):
    print(f"Hello, {name}!")
    print("Welcome to GitHub!")
    print(f"Your name has {len(name)} characters.")


if __name__ == "__main__":
    user_name = input("Please enter your name: ")
    greet(user_name)
