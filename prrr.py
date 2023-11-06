class Book:
    def __init__(self,id,name,quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

class User:
    def __init__(self,id,name,password):
        self.id = id
        self.name = name
        self.password = password
        self.borrowBook = []
        self.returnBook = []

class Library:
    def __init__(self,name):
        self.name = name
        self.users = []
        self.books = []
    
    def addBooks(self,id, name, quantity):
        book = Book(id, name, quantity)
        self.books.append(book)
        print(f'{book.name} added successfully \n')

    def addUser(self,id,name,password):
        user = User(id,name,password)
        self.users.append(user)
        return user

    def borrowBook(self,user,token):
        for book in self.books:
            if book.id == token:
                print(f'/t {book.name} book is already Borrowed \n')
            elif book.quantity == 0:
                print(f'No Copy is Available')
            else:
                user.b


bsk = Library('bisoo sahitto kendra\n')
admin = bsk.addUser(1000,'admin','admin')
ratin = bsk.addUser(17,'ratin','123')
cpBook = bsk.addBooks(11,'cp book',5)

currentUser = admin

while True:
    if currentUser == None:
        print('no user found')

    option = input('loggin or resister(L/R) : ')
    if option == 'L':
        id = int(input('enter id : '))
        password = input('enter your password : ')

        match = False
        for user in bsk.users:
            if user.id == id and user.password == password:
                currentUser = user
                match = True
                break    
        
        if match == False:
            print('No user Found')

    elif option == 'R':
        id = int(input('enter your id : '))
        name = input('Enter your Name : ')
        password = input('enter your password : ')
        
        for user in bsk.users:
            if user.id == id:
                print('user already exists')
        
        user = User(id,name,password)
        currentUser = user

    else:
        print(f'Welcome back {currentUser.name}\n')
        if currentUser.name == 'admin':
            print('Chose option')
            print('1. Add book')
            print('2. Add user')
            print('3. show all book')
            print('4. logout')

            ch = int(input('chose your option : '))
            if ch == 1:
                id = int(input("enter book id : "))
                name = input('Enter your book name : ')
                quantity = input('Enter number of book')

                book = bsk.addBooks(id,name,password)

            elif ch==2:
                id = int(input('Enter your id : '))
                name = input('Enter your name : ')
                password = input("enter your password : ")

                bsk.addUsers(id,name,password)

            elif ch==3:
                for book in bsk.books:
                    print(f'book name is ""{book.name}"" and its id no is {book.id}')

            elif ch==4:
                currentUser = None


        else:
            print('Chose option \n')
            print('1. Borrow book')
            print('2. Return book')
            print('3. Show already borrowed book')
            print('4. Show history')
            print('5. logout') 

            ch = int(input('Enter Option : '))

            if ch==1: