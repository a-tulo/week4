# print("Program Started!")
# user_char = input("Please enter a standard character\n")
#
# if len(user_char) == 1:
#     print(f"The ASCII code for {user_char} is {ord(user_char)}")
#
# print("Program Ended!")

print("Program Started!")

print("Please enter an ASCII code:")
code = int(input())

if code >= 32 and code <= 126:
    print(f"The character represented by the ASCII value {code} is: {chr(code)}")
else:
    print("The character cannot be displayed.")

print("Program Ended!")