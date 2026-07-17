def valid_password(password):

    minimum_length = len(password) >= 8
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)

    if minimum_length and upper and lower and digit:
          print("Password is valid")
          return True
    else:
        print("Password is invalid")
    if not minimum_length:
        print("1. Password should be at least 8 characters long")
    if not upper:
        print("2. Password should have at least one uppercase letter")
    if not lower:
        print("3. Password should have at least one lowercase letter")
    if not digit:
        print("4. Password should have at least one digit")
        return False

password = input("Enter a password to validate:")
valid_password(password)

