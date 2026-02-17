#Question:
# Password Strength Checker
# 
# Ask the user to enter a password until it is strong.  (A,S,A,K,R)
# 
# 
# Minimum 8 characters
# At least one digit
# At least one special character
# while loop → repeat until strong
# Nested if → check each condition
# elif → medium
# else → weak


print("====== PASSWORD STRENGTH CHECKER ======")

special_chars ="#123456@"

while True:   
    password = input("Enter your password: ")

    if len(password) >= 8:

        has_digit = False
        has_special = False

        for char in password:
            if char.isdigit():
                has_digit = True
            if char in special_chars:
                has_special = True

        #Nested if conditions
        if has_digit and has_special:
            print("Strong Password!")
            break

        elif has_digit or has_special:
            print("Medium Password (Add digit or special character)")

        else:
            print("Weak Password (Missing digit & special character)")

    else:
        print("Weak Password (Minimum 8 characters required)")
