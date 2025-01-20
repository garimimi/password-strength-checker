import string
import getpass

def check_pwd():
    while True:
        password = getpass.getpass("Enter Password: ")
        if len(password) < 8:
            print("Password must be at least 8 characters long. Please try again.")
        else:
            break

    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count +=1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count +=1
        else:
            special_count +=1

    if lower_count >= 1:
        strength +=1
    if upper_count >= 1:
        strength +=1
    if num_count >= 1:
        strength +=1
    if wspace_count >=1:
        strength +=1
    if special_count >=1:
        strength +=1

    if strength == 1:
        remarks = "poor security"
    elif strength == 2:
        remarks = "needs to be changed"
    elif strength ==3:
        remarks = "weak password"
    elif strength == 4:
        remarks = "can be stronger!"
    elif strength == 5:
        remarks = "strong passowrd"

    print('Your password has: ')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    print(f"Password Strength: {strength}")
    print(f"Hint: {remarks}")

def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
        choice = input('Do you want to enter another pwd (y/n): ')
    else:
        choice = input('Do you want to check pwd (y/n): ')

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid, Try Again')

if __name__ == '__main__':
    print('+++ Welcome to PWD Checker +++')
    ask_pw = ask_pwd()
    while ask_pw:
        check_pwd()
        ask_pw = ask_pwd(True)
