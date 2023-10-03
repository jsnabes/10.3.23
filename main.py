#Greeting and ask name
user_name = input("Hello! What is your name?  ")

# Print question and ask user to enter integer
prompt = int(input(f"Hi {user_name}. Enter an integer between 1 and 100: "))
numbers = range(0, 99)

# First option (build specification 2a)
for num in numbers:
    if prompt < 60 and prompt % 2 != 0:
        print(f"Thanks {user_name}. You entered {prompt}")
        print("Odd and less than 60")
        break

# Second option (build specification 2b)
    elif prompt < 25 and prompt > 1 and prompt % 2 == 0:
        print(f"Thanks {user_name}. You entered {prompt}")
        print("Even and less than 25")
        break

# Third option (build specification 2c)
    elif prompt > 25 and prompt < 61 and prompt % 2 == 0:
        print(f"Thanks {user_name}. You entered {prompt}")
        print("Even and between 26 and 60 inclusive")
        break

# Fourth option (build specification 2d)
    elif prompt > 60 and prompt % 2 == 0:
        print(f"Thanks {user_name}. You entered {prompt}")
        print("Even and greater than 60")
        break

# Fifth option (build specification 2e)
    elif prompt > 60 and prompt % 2 != 0:
        print(f"Thanks {user_name}. You entered {prompt}")
        print("Odd and greater than 60")
        break



