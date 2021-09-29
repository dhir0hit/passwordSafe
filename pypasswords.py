print("Welcome to password safe please Enter your access password")

# All the necessary global variables defined
user_choice = ["new-pass", "get-pass", "change-access", "update-pass", "del-pass"]  # some choices to run program
user_passwords = ""
access_pass = ""
password_count = ""
user_passwords_list = []
repeat_choice = True


def printing_userdata():
    print_count = 0
    count_list = ["st", "nd", "rd", "th"]
    found_data_list = []

    find_account = input("type name to update ")
    for user_data in user_passwords_list:
        if find_account in user_data:
            found_data_list.append(user_data)
            user_data = user_data.replace("\n", "")
            user_data = user_data.split(" ")

            print(f"{print_count + 1}{count_list[print_count] if print_count < 4 else count_list[3]} account")
            print()
            print(f"    Platform : {user_data[0]}")
            print(f"    Username : {user_data[1]}")
            print(f"    Email    : {user_data[2]}")
            print(f"    Password : {user_data[3]}")
            print()

            print_count += 1

    return found_data_list

def user_repeat_choice():
    global repeat_choice
    print("type 'yes' to run again or 'no' to exit")
    repeat_choice_check = True

    while repeat_choice_check:
        user_repeat_choice = input()
        if user_repeat_choice.lower() == "yes":
            repeat_choice = True
            repeat_choice_check = False

        elif user_repeat_choice.lower() == "no":
            repeat_choice = False
            repeat_choice_check = False

        else:
            print("your input unrecognized please try again from yes and no")


def director(access):
    global access_pass, password_count, user_passwords_list, repeat_choice
    if access == access_pass:
        print("Access Granted")
        print("What you want me to help with \nType help to get all valid functions you can use")
        repeat_choice = True
        while repeat_choice:
            user_file = open("user_access.txt", "r+")

            access_pass = user_file.readline()  # access password to program
            access_pass = access_pass.replace("\n", "")

            if not access_pass:
                access_pass = input("Write new access password to your safe > ")
                user_file.write(f"{access_pass}\n")

            password_count = user_file.readline()  # passwords in file default 0

            if not password_count:
                password_count = 0
                user_file.write("0")
            else:
                password_count = password_count.replace("\n", "")

            # user_passwords_list = user_file.read()
            # print(f"list = {user_passwords_list}")
            for i in range(int(password_count)):
                user_passwords_list.append(user_file.readline())
            # user_passwords = user_file.read()  # all user accounts
            user_file.close()

            choice = input("Type any function > ")
            if choice.lower() == "help":
                print(f"1. save new password : {user_choice[0]}")
                print(f"2. see all passwords or specific ones : {user_choice[1]}")
                print(f"3. change access of safe : {user_choice[2]}")
                print(f"4. update saved passwords : {user_choice[3]}")
                print(f"5. Delete password : {user_choice[4]}")

            elif choice.lower() == user_choice[0]:
                new_password()

            elif choice.lower() == user_choice[1]:
                get_passwords()

            elif choice.lower() == user_choice[2]:
                user_access_change()

            elif choice.lower() == user_choice[3]:
                password_update()

            elif choice.lower() == user_choice[4]:
                delete_password()
    else:
        print("Access Denied")
        main()

# --rohit--


def user_access_change():
    global user_passwords
    new_access = input("enter new access password > ")
    changing_pass = open("user_access.txt", "r")
    old_pass = changing_pass.readline()
    password_count = changing_pass.readline()
    user_passwords = changing_pass.read()
    changing_pass.close()

    changing_pass = open("user_access.txt", "w")
    changing_pass.write(f"{new_access}\n")
    for user_data in range(user_passwords_list):
        changing_pass.write(user_data)
    changing_pass.close()

    print(f"password changed to {new_access} from {old_pass}")
    user_repeat_choice()


def password_update():
    if user_passwords_list:
        found_data_list = printing_userdata()
        account_number = int(input("Enter account number to update")) - 1

        userData_delete = open("user_access.txt", "w")
        userData_delete.write(access_pass + "\n")
        userData_delete.write(str(password_count) + "\n")

        try:
            if found_data_list[account_number]:
                for i in range(len(user_passwords_list)):
                    if user_passwords_list[i] == found_data_list[account_number]:
                        user_temp_update = user_passwords_list[i].split(" ")

                        which_info_change = input("what information to change eg.Platform").lower()
                        if "platform" in which_info_change:
                            print("Enter a new Platform name")
                            update_platform = input("> ")
                            print(update_platform)
                            user_temp_update[0] = update_platform

                        if "username" in which_info_change:
                            print("Enter a new Username")
                            update_username = input("> ")
                            print()
                            user_temp_update[1] = update_username

                        if "email" in which_info_change:
                            print("Enter a new Email")
                            update_email = input("> ")
                            print()
                            user_temp_update[2] = update_email

                        if "password" in which_info_change:
                            print("Enter a new Password")
                            update_password = input("> ")
                            print()
                            user_temp_update[3] = update_password

                        if ("platform" not in which_info_change and "username" not in which_info_change
                                and "email" not in which_info_change and "password" not in which_info_change):
                            print("not recognized")
                            print("try from 'platform', 'username', 'email', 'password'")

                        user_passwords_list[i] = " ".join(user_temp_update)

                    userData_delete.write(user_passwords_list[i])
        except IndexError:
            print("unable find account please specify it again")

        if not found_data_list:
            for i in range(len(user_passwords_list)):
                userData_delete.write(user_passwords_list[i])

        userData_delete.close()
        user_repeat_choice()


def new_password():
    global password_count
    repeat_email = True
    unrecognized = True
    user_platform_repeat = True
    user_name_repeat = True

    print("Enter new information here if there is no information about username and email leave it empty")
    while user_platform_repeat:
        user_platform = input("Enter platform of account ")
        if user_platform.isspace():
            print("Dont enter space in name please try again")

        else:
            user_platform_repeat = False

    while user_name_repeat:
        user_name = input("Enter username ")
        if user_name == "":
            user_name_repeat = False

        elif user_name.isspace():
            print("Dont enter space in name please try again")

        else:
            user_name_repeat = False

    while repeat_email:
        user_email = input("Enter email ")
        if user_email == "":
            repeat_email = False

        elif user_email.isspace():
            print("Dont enter space in email please try again")

        elif "@" not in user_email:

            print()
            print("Expected @ in email")
            print(f"Want to keep the '{user_email}' or change?")
            print("Type 'Yes' to make change else 'No'. ")
            while unrecognized:
                change_input = input()

                if change_input.lower() == "no":
                    repeat_email = False
                    unrecognized = False

                elif change_input.lower() == "yes":
                    repeat_email = True
                    unrecognized = False

                else:
                    print("Unrecognized input please choose from yes or not")
                    unrecognized = True

        elif "@" in user_email:
            repeat_email = False

    new_user_password = input("Enter your password ")

    if not user_platform:
        print("Platform of account can not be empty")
    elif not user_name and not user_email:
        print("Please enter at least one of these Email or UserName")
    else:
        password_count = 1 + int(password_count)
        user_file = open("user_access.txt", "w")
        user_file.write(f"{access_pass}\n")
        user_file.write(f"{str(password_count)}\n")
        for i in user_passwords_list:
            user_file.write(i)
        user_file.close()

        if not user_name:
            user_name = "Na"
        if not user_email:
            user_email = "Na"

        user_file = open("user_access.txt", "a")
        user_file.write(f"{user_platform} {user_name} {user_email} {new_user_password}\n")
        user_file.close()

    user_repeat_choice()


def delete_password():
    global password_count

    if user_passwords_list:
        found_data_list = printing_userdata()

        account_number = int(input("Enter account number to delete")) - 1

        userData_delete = open("user_access.txt", "w")
        userData_delete.write(access_pass + "\n")
        password_count = 1 - int(password_count)
        userData_delete.write(str(password_count) + "\n")

        try:
            if found_data_list[account_number]:
                for i in range(len(user_passwords_list)):
                    if user_passwords_list[i] == found_data_list[account_number]:
                        del_info = found_data_list[account_number].split(" ")
                        print(f"Deleted account: {del_info}")
                    else:
                        userData_delete.write(user_passwords_list[i])
        except IndexError:
            print("Unable to find account please specify it again")

        if not found_data_list:
            for i in range(len(user_passwords_list)):
                userData_delete.write(user_passwords_list[i])

        userData_delete.close()
    user_repeat_choice()


def get_passwords():
    print_count = 0
    count_list = ["st", "nd", "rd", "th"]
    repeat_platform = True

    if user_passwords_list:
        find_account = input("which account you want to find or enter all ")
        for user_data in user_passwords_list:
            if find_account in user_data or find_account.lower() == "all":
                user_data = user_data.replace("\n", "")
                user_data = user_data.split(" ")

                for user_information in user_data:  # converts "Na" to "no information given"
                    if user_information == "Na":
                        user_information = "No information given"

                if find_account == user_data[0]:  # find if user gave platform name
                    if repeat_platform:  # finding if platform name is repeated or not
                        print()
                        print(f"Platform : {user_data[0]}")
                        print()
                        repeat_platform = False

                    print(f"{print_count + 1}{count_list[print_count] if print_count < 4 else count_list[3]} account")
                    print(f"    Username : {user_data[1]}")
                    print(f"    Email    : {user_data[2]}")
                    print(f"    Password : {user_data[3]}")
                    print()

                else:
                    print(f"{print_count + 1}{count_list[print_count] if print_count < 4 else count_list[3]} account")
                    print()
                    print(f"    Platform : {user_data[0]}")
                    print(f"    Username : {user_data[1]}")
                    print(f"    Email    : {user_data[2]}")
                    print(f"    Password : {user_data[3]}")
                    print()

                print_count += 1

    else:
        print("There are no passwords saved please add some passwords first.")

    user_repeat_choice()


def main():
    global access_pass
    global password_count
    global user_passwords_list

    try:
        user_file = open("user_access.txt", "r")  # file to read user passwords
    except FileNotFoundError:
        user_file = open("user_access.txt", "w")
        user_file.close()

        user_file = open("user_access.txt", "r")

    access_pass = user_file.readline(4)
    user_file.close()

    user_access = input("type your access pass > ")

    director(user_access)


if __name__ == "__main__":
    main()
    #---rohit---
