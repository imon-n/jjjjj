class Book:
    def __init__(self,id,name,quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

class User:
    def __init__(self,id,name, password):
        self.id = id
        self.name = name
        self.password = password
        self.borrowedBook = []
        self.returnedBook = []

class Library:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.books = []

    def addBooks(self, id, name, quantity):
        book = Book(id,name,quantity)
        self.books.append(book)
        print(f'{book.name} added successfully \n')

    def addUsers(self, id, name, password):
        user = User(id,name,password)      
        self.users.append(user)
        return user

    def borrowBook(self,user,token):
        for book in self.books:
            if book.id == token:
                if book in user.borrowedBook:
                    print('already borrowed \n')
                    return
                
                elif book.quantity == 0:
                    print('No Copy Available \n')
                    return

                else:
                    user.borrowedBook.append(book)
                    book.quantity -= 1
                    print('Borrowed book Successfully \n')
                    return
        print(f'Not found any book with name {token}! \n') 


    def returnBook(self,user,token):
        for book in self.books:
            if book.id == token:
                if book in user.borrowedBook:
                    book.quantity += 1
                    user.returnedBook.append(book)
                    user.borrowedBook.remove(book)
                    print('Return book Successfully \n')
                    return
                
                else:
                    print(f"\n\t---> !!! You are not reading {book.name} now")
                    return
        print(f'Not found any book with name {token}! \n')    


bsk = Library('Bisso sahitto kendro')
admin = bsk.addUsers(1000, 'admin', 'admin')
ratin = bsk.addUsers(17,'ratin', '123')
cpBook = bsk.addBooks(11,'cp book',5)

currentUser = admin

while True:
    if currentUser == None:
        print('no loggen in user \n')

        option = input('loggin or register (L/R) :')
        if option == 'L':
            id = int(input("Enter Id : "))
            password = input("Enter Password : ")

            match = False
            for user in bsk.users:
                if user.id == id and user.password == password:
                    currentUser = user
                    match = True
                    break           
            if match == False:
                print('No user found\n')

        elif option == 'R':
            id = int(input("Enter Id : "))
            name = input("Enter name : ")
            password = input("Enter Password : ")

            for user in bsk.users:
                if user.id == id:
                    print('user already exists!\n')
                    # break
            user = bsk.addUsers(id,name,password)
            currentUser = user

    else:
        print(f'welcome Back {currentUser.name} \n')
        if currentUser.name == 'admin':
            print('chose option\n')
            print('1: Add book')
            print('2: Add User')
            print('3: Show all book')
            print('4: logout')

            ch = int(input("enter option : "))
            if ch==1:
                id = int(input('Enter book id : '))
                name = input('Enter book name : ')
                quantity = input('Enter number of book : ')

                bsk.addBooks(id,name,quantity)

            elif ch==2:
                id = int(input('Enter your id : '))
                name = input('Enter your name : ')
                password = input("enter your password : ")

                bsk.addUsers(id,name,password)

            elif ch==3:
                for book in bsk.books:
                    print(f'{book.id}\t{book.name}\t{book.quantity}')
                print('\n')

            elif ch==4:
                currentUser = None

        else:
            print('chose option\n')
            print('1: Borrow book')
            print('2: Return Book')
            print('3: Show Borrowed all book')
            print('4: Show History')
            print('5: logout')

            ch = int(input('Enter Option : '))

            if ch == 1:
                id = int(input("\tEnter book id : "))
                bsk.borrowBook(currentUser,id)

            elif ch == 2:
                id = int(input("\t Enter book id : "))
                bsk.returnBook(currentUser,id)

            elif ch == 3:
                print('\n\t Borrowed Books showing : \n')
                for book in currentUser.borrowedBook:
                    print(f'\t{book.id}\t{book.name}\t{book.quantity}')

            elif ch == 4 :
                for book in currentUser.returnedBook:
                    print(f'\t{book.id}\t{book.name}\t{book.quantity}')

            elif ch == 5:
                currentUser = None

            else:
                print(f'\n\t---> !!! Choose valid option \n')




        ####### if you want you can add for extra feature ########### (not mendatory)



            # elif ch==4:
            #     print("\n\t All Books:\n")
            #     for book in bsk.books:
            #         if book in currentUser.borrowedBooks:
            #             print(f'\t{book.id}\t{book.name}\t{book.quantity}\tReading Now..')
            #         elif book in currentUser.returnedBooks:
            #             print(f'\t{book.id}\t{book.name}\t{book.quantity}\tAlready Read')
            #         else:
            #             print(f'\t{book.id}\t{book.name}\t{book.quantity}\tDid not Read')
