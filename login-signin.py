# Saved items:
Email = "aan@email.com"
Password = 12345678
error_count = 0
error_limit = 2
# Lol, I meant retry_count and retry_limit

# Work beginning
login_or_sign_in = input("What do you want? (L)og in or (S)ign in: ")
if login_or_sign_in.upper() == "L":
    # Lol, over-engineering!
    
    email = input("Email: ")
    if email == Email:
        while error_count < error_limit:
            password = int(input("Password: "))
            error_count += 1
            if password == Password:
                print("You're successfully logged in.")
                break
            else:
                print("wrong password.Try again.")
    else:
        print("Wrong email address.Try again.")
        email = input("Email: ")
        if email == Email:
            while error_count < error_limit:
                password = int(input("Password: "))
                error_count += 1
                if password == Password:
                    print("You're successfully logged in.")
                    break
                else:
                    print("wrong password.Try again.")
        else:
            print("Wrong email address.Try again.")

elif login_or_sign_in.upper() == "S":
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email_address = input("Email: ")
    retype_email = input("Confirm your email address: ")
    if email_address == retype_email:
        password = input("Password (at least 8 digit): ")
        if len(password) == 8:
            retype_password = input("Confirm your password: ")
            if int(password) == int(retype_password):
                print(f"Dear {first_name}, you're successfully signed in.")
            else:
                print("Sorry, password doesn't match with previous one. please, try again.")
        else:
            print('Password is too short.')
            password = input("Password: ")
            retype_password = input("Confirm your password: ")
            if int(password) == int(retype_password):
                print(f"Dear {first_name}, you're successfully signed in.")
            else:
                print("Sorry, password doesn't match with previous one. Please, try again.")
    else:
        print("Sorry, your email doesn't match with previous one. Please, try again.")
else:
    print("We doesn't understand your command. Please, try again.")

# See https://github.com/ahnafalnafis/auth-system which was inspired by this project
