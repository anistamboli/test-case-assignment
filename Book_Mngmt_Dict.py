#Create, Add, remove and search book in a basic book records system...


rec={'1':"Naruto - Masashi Kishimoto ",'2':"Shingeki no Kyojin - Hajime Isayama",'3':"DB series - Akira Toriyama",'4':"Berserk - Miura",'5':"Vinland Saga - Makoto Yukimura", '6':"Kimi no nawa - Makoto Shinkai"}

def createBk():
    rec.clear()
    print("new book system created...")
    print(rec)

    
def addBk():
    bookId= input("Enter book id to add : ")
    if bookId in rec:
        print("Book already exists")
    else:
        bookName= input("Enter book name to add : ")
        rec[bookId]=bookName
        print("Book added successfully...")


def removeBk():
    bookId=input("Enter book id to remove book : ")
    if bookId in rec:
        rec.pop(bookId)
        print("book removed successfully...")
    else:
        print("Book not found!!!")
    

def search():
    bookId= input("Enter id of book to search: ")
    if bookId in rec:
        print(bookId," is a book naming : ", rec[bookId])
    else:
        print("Book not found!!!")

    
def bk_management_system():
    response = input('Enter choice : ')
    while(True):
        if response=='1':
            createBk()
        elif response=='2':
            addBk()
        elif response=='3':
            removeBk()
        elif response=='4':
            search()
        elif response=='5':
            print(rec)
        else:
            print("ok confirm exit...  ")
            exit()
        bk_management_system()

print("All books: ",rec)
print("\ntype: 1.create new Book system  2.add book  3.remove book  4.search book  5.show all books  .anythyng to exit : \n")
bk_management_system()
