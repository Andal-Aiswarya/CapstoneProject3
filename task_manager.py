# =====importing libraries===========
from datetime import date
import datetime
import os.path


# Creating function for registering new user
def reg_user():

    # Checking if the username is admin or not, and admin only can register new users
    if user_name != 'admin':
        print(f"{CRED}You are not allowed to register a user! Please contact admin!!{CEND}")
    else:

        # Open file user text and read all datas and declaring usernames list for appending all usernames in list
        with open('user.txt', 'a+') as file1:
            file1.seek(0)
            user_data = file1.readlines()
            usernames1 = []
            for line1 in user_data:
                split_data1 = line1.split(", ")
                usernames1.append(split_data1[0])

            #  checking username already exists or not, and taking username if not already exists.
            while True:
                name = input("Enter the user name: ")
                if name not in usernames1:

                    # Confirming password twice and registering successfully
                    while True:
                        password_ = input("Enter the password you would like to give: ")
                        password_1 = input("Enter the password again: ")
                        if password_ != password_1:
                            print(f"{CRED}passwords does not match! Try again{CEND}")
                            continue
                        else:
                            file1.write(f"{name}, {password_}\n")  # write name and password into user,txt file
                            print(f"{CGREEN}Your username and password are successfully registered!!{CEND}")
                        break

                else:
                    print(f"{CRED}Username already taken. Try another.{CEND}")
                    continue
                break
        file1.close()


# Creating function for adding new task to users
def add_task():
    with open('tasks.txt', 'a+') as file2:

        # get all data from user and write into file
        username = input("Enter the user name of person whom the task is assigned to: ")
        task = input("Enter the title of the task: ")
        description = input("Enter the description of the task: ")
        due_date = input("Enter the due date of the task in format(e.g. 01 Jan 1990):")
        current_date = date.today()
        file2.write(f"{username}, {task}, {description}, {due_date}, {current_date}, No\n")
        print(f"{CGREEN}Your new task has been successfully added!!{CEND}")
    file2.close()


# Creating function for viewing all tasks of all users
def view_all():
    with open('tasks.txt', 'r+') as file3:
        data = file3.readlines()

        # use pos and enumerate function to establish numbers
        for pos, line in enumerate(data, 1):
            split_data = line.split(", ")
            output = f"─────────────────────[{pos}]────────────────────────────────────\n"
            output += f"Task:                {split_data[1]}\n"
            output += f"Assigned to:         {split_data[0]}\n"
            output += f"Date assigned:       {split_data[4]}\n"
            output += f"Due date:`           {split_data[3]}\n"
            output += f"Task completed?      {split_data[5]}\n"
            output += f"Task description:    {split_data[2]}\n"
            output += f"────────────────────────────────────────────────────────────────"
            print(output)
    file3.close()


# Creating function for viewing user's own tasks and editing it
def view_mine():

    # Opening tasks file and creating username list
    with open('tasks.txt', 'r') as file4:
        data = file4.readlines()
        usernames = []
        for line in data:
            split_data = line.split(", ")
            usernames.append(split_data[0])

        # use pos and enumerate function to establish numbers and print user's own task
        for pos, line in enumerate(data, 1):
            split_data = line.split(", ")
            if user_name in usernames:
                if user_name == split_data[0]:
                    output = f"──────────────[{pos}]───────────────\n"
                    output += f"Task:                {split_data[1]}\n"
                    output += f"Assigned to:         {split_data[0]}\n"
                    output += f"Date assigned:       {split_data[4]}\n"
                    output += f"Due date:`           {split_data[3]}\n"
                    output += f"Task completed?      {split_data[5]}\n"
                    output += f"Task description:    {split_data[2]}\n"
                    output += f"────────────────────────────────────"
                    print(output)
            else:
                print(f'{CGREY}No tasks assigned for you !!{CEND}')
                main_menu()
                break

        # Creating options for editing data or back to main menu
        display_1 = "────────────────────[Select a option]─────────────────────\n"
        display_1 += "1 : To edit a specific task\n"
        display_1 += "-1 : Return to main menu\n"
        display_1 += "Enter a number option: "
        while True:
            to_edit_data = int(input(f"{CBLUE}{display_1}{CEND}"))
            if to_edit_data == 1:
                task_num = int(input(f"{CGREY}Enter the task number to be edited: {CEND}"))-1
                edit_data = data[task_num]
                split_data_edit = edit_data.split(", ")
                if split_data_edit[0] == user_name:
                    if split_data_edit[-1] == 'No\n':

                        if task_num < 0 or task_num >= len(data):
                            print(f"{CRED}Enter valid task option{CEND}")
                        elif data[task_num] == 'Yes\n':
                            print(f"{CYELLOW}Task Already Completed{CEND}")
                        else:
                            display_2 = "────────────────────[Select a option]─────────────────────\n"
                            display_2 += "1 : Mark the task as complete\n"
                            display_2 += "2 : Edit the task\n"
                            display_2 += "Enter a number option: "

                            # Asking user to select option from edit the task or mark as completed
                            while True:
                                choice = int(input(f"{CGREY}{display_2}{CEND}"))

                                if choice <= 0 or choice >= 3:
                                    print(f"{CRED}Invalid option, try again!{CEND}")

                                    continue
                                elif choice == 1:
                                    edit_data = data[task_num]
                                    if task_num <= -1 or task_num >= len(data):
                                        print(f"{CRED}Invalid task option, try again!{CEND}")
                                        continue
                                    else:
                                        split_data_ = edit_data.split(", ")
                                        split_data_[-1] = 'Yes\n'
                                        new_data = ", ".join(split_data_)
                                        data[task_num] = new_data
                                        file4 = open('tasks.txt', 'w+')
                                        for line in data:
                                            file4.write(line)
                                        print(f"{CGREEN}Your new data has been updated!!{CEND}")
                                        break
                                elif choice == 2:

                                    # Asking user to select which data to be edited and which part to be edited.
                                    while True:
                                        display = "────────────────────[Select a option]─────────────────────\n"
                                        display += "1 : To edit username\n"
                                        display += "2 : To edit due date\n"
                                        display += "-1 : To main menu\n"
                                        display += "Enter number  option to edit data: "
                                        choice_edit = int(input(f"{CYELLOW}{display}{CEND}"))
                                        edit_data = data[task_num]

                                        # coding to edit user name
                                        if choice_edit == 1:
                                            username_new = input(f"{CGREY}Enter new username:{CEND} ")
                                            split_data_ = edit_data.split(", ")
                                            split_data_[0] = username_new
                                            new_data = ", ".join(split_data_)
                                            data[task_num] = new_data
                                            file5 = open('tasks.txt', 'w+')
                                            for line in data:
                                                file5.write(line)
                                            file5.close()
                                            print(f"{CGREEN}Your new data has been updated!!{CEND}")
                                            main_menu()

                                        # To edit due date
                                        elif choice_edit == 2:
                                            due_date_new = input(f"{CGREY}Enter new due date in format (e.g.) 01 Jan 1990: {CEND}")
                                            split_data_ = edit_data.split(", ")
                                            split_data_[3] = due_date_new
                                            new_data = ", ".join(split_data_)
                                            data[task_num] = new_data
                                            file6 = open('tasks.txt', 'w+')
                                            for line in data:
                                                file6.write(line)
                                            file6.close()
                                            print(f"{CGREEN}Your new data has been updated!!{CEND}")
                                            main_menu()
                                        elif choice_edit == -1:
                                            main_menu()
                                        else:
                                            print(f"{CRED}Please enter valid option{CEND}")
                                            continue
                    else:
                        print(f"{CYELLOW}The task has been completed already!!!{CEND}")
                else:
                    print(f"{CRED}You are not allowed to edit others task!{CEND}")
                    continue
            elif to_edit_data == -1:
                main_menu()
            else:
                print(f"{CRED}Enter valid option{CEND}")
                continue
            break

    file4.close()


# Creating function for generating report for admin
def generate_report():

    # Declare today date and day format
    today = datetime.datetime.today()
    date_format = '%d %b %Y'

    # create file 'task overview'
    with open('task_overview.txt', 'w+') as t_o:
        file8 = open('tasks.txt', 'r')
        data = file8.readlines()

        # Finding total number of tasks and completed and incomplete details and writing in task overview text files
        t_o.write(f"The total number of tasks is: {len(data)}\n")
        completed = 0
        uncompleted = 0
        for line in data:
            split_data = line.split(", ")
            if split_data[-1] == 'Yes\n':
                completed += 1
            else:
                uncompleted += 1
        t_o.write(f"The total number of completed tasks are: {completed}\n")
        t_o.write(f"The total number of uncompleted tasks is: {uncompleted}\n")

        # Finding tasks overdue and percentage of tasks not completed and tasks overdue
        over_due = 0
        for line in data:
            split_data = line.split(", ")
            that_date = split_data[-3]
            due_date = datetime.datetime.strptime(that_date, date_format)
            if split_data[-1] == 'No\n':
                if due_date < today:
                    over_due += 1
        t_o.write(f"The total number of tasks that haven’t been completed and that are overdue is: {over_due}\n")
        incomp_percentage = (uncompleted / len(data)) * 100
        t_o.write(f"The percentage of tasks that are incomplete: {round(incomp_percentage, 2)}%\n")
        overdue_percentage = (over_due / len(data)) * 100
        t_o.write(f"The percentage of tasks that are overdue: {round(overdue_percentage, 2)}%\n")
    t_o.close()
    file8.close()

    # Creating file 'user overview'
    with open('user_overview.txt', 'w+') as u_o:
        file9 = open('user.txt', 'r')
        user_data = file9.readlines()
        file10 = open('tasks.txt', 'r')
        task_data = file10.readlines()
        # Creating total number of users registered and tasks tracked
        u_o.write(f"The total number of users registered is: {len(user_data)}\n")
        u_o.write(f"The total number of tasks generated and tracked is: {len(task_data)}\n")

        # Creating user_task dictionary and creating task count for each user
        user_task = {}
        for line in user_data:
            split_data = line.strip().split(", ")
            user_task[split_data[0]] = 0
        for name in user_task:
            task_count = 0
            for line1 in task_data:
                split_data_1 = line1.strip().split(", ")
                if name == split_data_1[0]:
                    user_task[name] = task_count + 1
                    task_count += 1
        # Creating user_compl dictionary and creating task completed for each user
        user_compl = {}
        for line in user_data:
            split_data = line.strip().split(", ")
            user_compl[split_data[0]] = 0
        for name in user_compl:
            compl_count = 0
            for line1 in task_data:
                split_data_1 = line1.strip().split(", ")
                if name == split_data_1[0] and split_data_1[-1] == 'Yes':
                    user_compl[name] = compl_count + 1
                    compl_count = compl_count + 1

        # Creating formula for creating task not completed for each user
        user_uncompl = {key: user_task[key] - user_compl.get(key, 0) for key in user_task.keys()}

        # Creating uncompl_overdue dictionary and creating task overdue for each user
        uncompl_overdue = {}
        for line in user_data:
            split_data = line.strip().split(", ")
            uncompl_overdue[split_data[0]] = 0
        for name in uncompl_overdue:
            overdue_count = 0
            for line1 in task_data:
                split_data_1 = line1.strip().split(", ")
                that_date = split_data_1[-3]
                due_date = datetime.datetime.strptime(that_date, date_format)
                if name == split_data_1[0] and split_data_1[-1] == 'No' and due_date < today:
                    uncompl_overdue[name] = overdue_count + 1
                    overdue_count += 1

        # Writing all details required in file user overview
        for names in user_task:
            u_o.write(f"----------------[{names}]----------------------------\n")
            u_o.write(f"The total number of tasks assigned to {names} is : {user_task[names]}\n")
            user_task_percent = (user_task[names] / len(task_data)) * 100
            u_o.write(f"The percentage of tasks assigned to {names} is : {round(user_task_percent, 2)}%\n")

            # Here using if/else condition to avoid error for tasks not assined for user time( to avoid divided by zero)
            if user_task[names] == 0:
                u_o.write(f"The percentage of tasks assigned to {names} that have been completed is:0.0%\n")
                u_o.write(f"The percentage of tasks assigned to {names} that must still be completed is:0.0%\n")
                u_o.write(
                    f"The percentage of tasks assigned to {names} that have not yet been completed and are overdue is: 0.0%\n")
            else:
                user_compl_percent = (user_compl[names] / user_task[names]) * 100
                u_o.write(
                    f"The percentage of tasks assigned to {names} that have been completed is:{user_compl_percent}%\n")
                user_uncompl_percent = (user_uncompl[names] / user_task[names]) * 100
                u_o.write(
                    f"The percentage of tasks assigned to {names} that must still be completed is: {user_uncompl_percent}%\n")
                uncom_overdue_percent = (uncompl_overdue[names] / user_task[names]) * 100
                u_o.write(
                    f"The percentage of tasks assigned to {names} that have not yet been completed and are overdue is: {uncom_overdue_percent}%\n")
    print(f"{CGREEN}Your reports are created. Please check text files!!{CEND}")
    u_o.close()
    file9.close()
    file10.close()


# Creating function for generating stats from user and tasks text files for admin
def stats_():

    # Assign file path
    file_path = r'C:\Users\rAAm\PycharmProjects\pythonProject\task_overview.txt'

    # If file exists, data from specified files are displaying as output
    flag = os.path.isfile(file_path)
    if flag:
        with open('task_overview.txt', 'r') as f:
            task_overview = f.readlines()
        print(f"{CYELLOW}─────────────────────[Task Overview]─────────────────────{CEND}")
        for data in task_overview:
            task_ov = data.rstrip()
            print(f"{task_ov}", end="" + "\n")
        with open('user_overview.txt', 'r') as f1:
            user_overview = f1.readlines()
        print(f"{CYELLOW}────────────────────[User Overview]─────────────────────{CEND}")
        for data1 in user_overview:
            user_ov = data1.rstrip()
            print(f"{user_ov}", end="" + "\n")
        f.close()
        f1.close()

    # If file not exists, going back to generate report and then data from specified files are displaying as output
    else:
        generate_report()
        with open('task_overview.txt', 'r') as f:
            task_overview = f.readlines()
        print(f"{CYELLOW}─────────────────────[Task Overview]─────────────────────{CEND}")
        for data in task_overview:
            task_ov = data.rstrip()
            print(f"{task_ov}", end="" + "\n")
        with open('user_overview.txt', 'r') as f1:
            user_overview = f1.readlines()
        print(f"{CYELLOW}─────────────────────[User Overview]─────────────────────{CEND}")
        for data1 in user_overview:
            user_ov = data1.rstrip()
            print(f"{user_ov}", end="" + "\n")
        f.close()
        f1.close()


# Creating function for main menu
def main_menu():
    while True:

        # presenting the menu to user and admin separately(To provide gr & ds menu). Converting user input to lowercase.
        if user_name != 'admin':
            menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()
        else:
            menu = input('''Select one of the following Options below:
                r - Registering a user
                a - Adding a task
                va - View all tasks
                vm - view my task
                gr - Generate Reports
                ds - Display Statistics
                e - Exit   
                : ''').lower()

    # For admins alone, registering a user into file user.txt , open file and use 'a+' to write data
        if menu == 'r':
            if user_name != 'admin':
                print("You are not allowed to register a user! Please contact admin!!")
            else:
                reg_user()

        # Adding task into file tasks.txt, open file and use 'a+' to write data
        elif menu == 'a':
            add_task()

        # Viewing all tasks from file tasks.txt, open file and use 'r' to read data
        elif menu == 'va':
            view_all()

        # viewing my tasks from file tasks.txt, open file and use 'r' to read data
        elif menu == 'vm':
            view_mine()

        # assigning e to get exit from menu
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        elif menu == 'gr':
            generate_report()

        #statistics to admin
        elif menu == 'ds' and user_name == 'admin':
           stats_()

        # if user typed somthing not from menu option, print below statement
        else:
            print("You have made a wrong choice, Please Try again")


# Declaring colors and style to use throughout the program
CEND = '\33[0m'
CBOLD = '\33[1m'
CITALIC = '\33[3m'
CRED = '\33[31m'
CGREEN = '\33[32m'
CYELLOW = '\33[33m'
CBLUE = '\33[34m'
CGREY = '\33[90m'

# ====Login Section====
# Read data from user.txt file
with open('user.txt', 'r') as file:
    data = file.readlines()

    # Declare a dictionary variable for storing username and password
    user_pass = {}
    for line in data:

        # Split data and store username as keys and password as values respectively
        split_data = line.strip().split(", ")
        user_name = user_pass.keys()
        pass_word = user_pass.values()
        user_pass[split_data[0]] = split_data[1]
    while True:

        # To login ask user to input username and password
        user_name = input("Enter your username: ")
        pass_word = input("Enter your password: ")

        # Check if username and password match else print appropriately
        if user_name in user_pass:
            if user_pass[user_name] == pass_word:
                break
            else:
                print("Your password is incorrect!! Please try again")
        else:
            print("Please enter valid username!!")
file.close()
main_menu()