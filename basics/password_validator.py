username = input("enter your username:")
password = input("enter your password:")
# Check password length
if len(password) >= 8:
    print("your password had 8 characters")
else:
    print("Your password is too short. It should be at least 8 characters.")
# Check if password contains a number
has_digit = False
for char in password:
    if char.isnumeric():
        has_digit = True
        break
if has_digit:
        print("your password contains a digit")
else:
    print("Your password does not contain any digits.")