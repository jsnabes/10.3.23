# Get integer
print("Learn your squares and cubes!")
keep_going = "y"
# Continue asking user to enter an integer
while keep_going.lower() == "y":
    prompt = int(input("Enter an integer: "))
# Print table results
    print("Number   Squared     Cubed")
    print("======   =======     =====")
    for i in range(prompt):
        i += 1
        print(f"{i}         {i ** 2}          {i ** 3}")

# # Extended challenge  ** Couldn't quite figure it out but tried!
#     print("Here's a multiplication table for reference!")
# # Print horizontal lines of multi table
#     horizontal = ""
#     for i in range(prompt):
#         i += 1
#         horizontal += str(i) + "    "
#         print(horizontal)
#  # Print vertical lines of multi table
#     for i in range(prompt):
#         i += 1
#     print(f"{i}   |    {i * 1}    {i * 3}     {i * 4}")

# Ask to continue. If n program will end
    keep_going = input("Continue? (y/n): ")




