#LIBRARY.PY

books={}
issue_books={}

def add_books():
    name=input("enter the name of books: ")
    books[name] = "available"
    print("books added")
def show_books():
    if len(books)==0:
        print("no books available")
    else:
        print("books available")
        for b in books:
            print(b)
def issued_books():
    show_books()
    name=input("enter the name of the book: ")
    if name in books:
        issue_books[name] = books.pop(name)
        print("book issued")
    else:
        print("book not issued")
def return_books():
    name=input("enter the name of the book: ")
    if name in issue_books:
        books[name] = issue_books.pop(name)
        print("books returned")
    else:
        print("no books to return")

#MAIN BODY!
def library():
    while True:
        print("\n 1.Add books")
        print("2.Show books")
        print("3.Issued books")
        print("4.Return books")
        print("5.Exit")

        choice=int(input("enter the value of choice: "))
        
        if choice==1:
            add_books()
        elif choice==2:
            show_books()
        elif choice==3:
            issued_books()
        elif choice==4:
            return_books()
        elif choice==5:
            print("thank you")
            break
        else:
            print("invalid choice")
library()
