books=[]

while True:
    print("1.Add 2.View 3.Exit")
    c=input()

    if c=="1":
        books.append(input("Book name: "))
    elif c=="2":
        print(books)
    else:
        break
