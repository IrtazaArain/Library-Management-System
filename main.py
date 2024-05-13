import csv


book_list= []
users=[]

def display_menu():
    print("--------------------------------------")
    print(" Welcome to Library Management System")
    print("---------------------------------------")
    print("\nPlease select an option: \n")
    print("1. View Books")
    print("2. Search Book")
    print("3. Sign in")
    print("4. Create An Account")
    print("5. Admin Portal")
    print("6. Quit")


def Books():
    print('-' * 90)
    print('{:<5s}{:^30s}{:^20s}{:^25s}{:>10s}'.format('No', 'TITLE', 'AUTHOR', 'SUBJECT', 'PUBLISHED'))
    print('-' * 90)
    count = 0
    for book in (book_list):
        count += 1
        print('{:<5s}{:<30s}{:^20s}{:<25s}{:>10s}'.format(str(count), book[0], book[1], book[2], book[3]))
    input("\nPress Enter to continue")

def Search():
    print('Search by:\n    1. Title\n    2. Author\n    3. Subject\n    4. Publication Date\n    5. Exit\n')
    x = int(input('Enter number of your selection: '))
    s = input('Enter your query: ')

    def search_by(s):
        print('-' * 90)
        print('{:<5s}{:^30s}{:^20s}{:^25s}{:>10s}'.format('No.', 'TITLE', 'AUTHOR', 'SUBJECT', 'PUBLISHED'))
        print('-' * 90)
        count = 0
        for i in range (len(book_list)):
            if s in book_list[i][x-1]:
                count += 1
                print('{:<5s}{:<30s}{:^20s}{:<25s}{:>10s}'.format(str(count), book_list[i][0], book_list[i][1], book_list[i][2], book_list[i][3]))
        return ''
    return search_by(s)

def members(user):
    user_data=user
    def res(book_name):
        user_data.append("Reserved: "+book_name)
        print("\nBook has been reserved for you. We'll let you know when it's available for you.\nThank you for your cooperation!")
        return ''

    def reserve():
        r = input("Enter book name with author's name that you want to reserve: ")
        return res(r)

    def borrow():
        b=input("Enter Book Title: ")
        for i in (book_list):
            if i[0] == b:
                user_data.append("Borrowed: " +b)
                print("Book issued in your name. Happy Reading!!")
                return ''
        print("Book not found")
        c = input("Would you like to have it reserved for you when it arrives? (Yes/No): ")
        if c == 'y' or c == 'Y' or c == 'Yes' or c == 'yes' or c == 'YES':
            print(res(b))
        else:
            return "Book not reserved. Returning to Members' Area...\n"

    def Return():
        b = input('Enter title of book you want to return: ')
        count = 1
        for i in user_data[2:]:
            count += 1
            if b in i:
                del user_data[count]
                print("Book has been returned to the bookshelf. We hope you enjoyed it.")
                return ''
        print("Book not found in your account. Returning to Members' Area...")
        return ''

    def renew():
        b = input('Enter title of the book you want to return: ')
        count = 0
        for i in user_data[2:]:
            if b in i:
                count+=1
                break
        if count > 0:
            print("Due date has been extended. Enjoy your book!!")
            return ''
        else:
            print("Book not found in your account. Returning to Members' Area...")
            return ''

    print ("\nWelcome Back\n________________\n")
    while True:
        print("Members' Area:\n\n    1. Borrow A Book\n    2. Return A Book\n    3. Renew A Book\n    4. Reserve A Book\n    5. Exit\n")
        z = int(input('Enter the number of your selection: '))
        if z == 1:
            print(borrow())
        elif z == 2:
            print(Return())
        elif z == 3:
            print(renew())
        elif z == 4:
            print(reserve())
        else:
            print('Exiting...')
            count = 0
            for i in users:
                if i[0] == user_data[0]:
                    del users[int(count)]
                    users.append((user_data))
                count += 1

def sign_in():
    print("\nPlease Sign In\n_____________________\n")
    while True:
        count=0
        usr=input('Enter your username: ')
        paswd=input('Enter your password: ')
        for i in users:
            if usr == i[0] and paswd == i[1]:
                print("\nLogin Successful!!\n")
                print(members(i))
            elif count < (len(users)-1):
                count+=1
            else:
                print("\nAccount Not Found!!\nIf you are a member, please try again...")
        y = input("Enter any key to retry or 'E' to exit: ")
        if y == 'e' or y == 'E':
            break
        else:
            continue

def new_account():
    usr = input('\nEnter a username for your account: ')
    paswd = input('Set a strong password: ')
    for i in users:
        if usr == i[0]:
            print("\nUsername Already Taken! Try a different one.\n")
            return new_account()
    users.append([usr,paswd])
    with open('Accounts.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(users)
    input("\nAccount created successfully\nPress Enter to continue")


def admin():

    def add_book():
        t=input('Enter title of new book: ')
        n=input('Enter name of author: ')
        s=input('Enter subject: ')
        d=input('Enter date of publication (dd/mm/yyyy): ' )
        new_book=[t,n,s,d]
        book_list.append(new_book)
        with open ('Books.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(book_list)
        return "New book has been added to database"

    def edit_book():
        print(Books())
        n = input('Enter number of book you want to edit: ')
        print('Edit:\n    1. Ttile\n    2. Author\n    3. Subject\n    4. Publishing Date')
        y = input("Enter your choice number: ")
        new = input("\nEnter edited version of selection: ")
        book_list[int(n)-1][int(y)-1] = new
        with open('Books.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(book_list)
        return "Your changes have been saved"

    def rm_book():
        print(Books())
        n = input ('Enter the number of book you want to delete: ')
        del book_list[int(n)-1]
        with open('Books.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(book_list)
        return "Book has been deleted"

    def rm_user():
        n = input('Enter username of user account you want to delete: ')
        for i in users:
            count = 0
            if n == i[0]:
                del users[i]
                with open('Accounts.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(users)
            elif count < (len(users) - 1):
                count += 1
            else:
                return "Account not found!!"

    while True:
        
        print("\nAdmin Portal\n________________")
        print(
            "\nPlease select an option:\n    1. Add A Book\n    2. Edit A Book\n    3. Remove A Book\n    4. Delete An Account\n    5. Exit Admin Portal\n")
        selection = int(input('Enter Number of your selection: '))
        if selection > 0 and selection < 6:
            if selection == 1:
                add_book()
            elif selection == 2:
                edit_book()
            elif selection == 3:
                rm_book()
            elif selection == 4:
                rm_user()
            else:
                break
        else:
            input("Wrong selection press Enter to continue")
            
while True:
    display_menu()
    books = open('Books.csv', 'r')
    r1 = csv.reader(books)
    book_list = list(r1)

    f = open('Accounts.csv', 'r')
    r2 = csv.reader(f)
    users = list(r2)
    
    selection = int(input ('\nEnter Number of your selection: '))
    if selection > 0 and selection < 7:
        if selection == 1:
            Books()
        elif selection == 2:
            Search()
        elif selection == 3:
            sign_in()
        elif selection == 4:
            new_account()
        elif selection == 5:
            admin()
        else:
            break
    else:
        
        input("Wrong selection press Enter to continue\n")
        
print("\n-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
