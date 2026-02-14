import datetime

class Management:
    def __init__(self, name, book,phone,Email):
        self.name = name
        self.book = book
        self.phone= phone
        self.Email= Email
        self.issued_date = datetime.datetime.now()
        self.return_date = self.issued_date + datetime.timedelta(days=10)

    def display(self):
        print("======================")
        print("Name:", self.name)
        print("Book:", self.book)
        print("phone:",self.phone)
        print("email:",self.Email)
        print("Issued Date:", self.issued_date.strftime("%d-%m-%Y"))
        print("Return Date:", self.return_date.strftime("%d-%m-%Y"))

name = input("Enter student name: ")
book = input("Enter book title: ")
phone=input("enter your phone:")
Email=input("enter your email:")

x1 = Management(name, book ,phone ,Email)
x1.display()