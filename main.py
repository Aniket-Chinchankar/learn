def person(name , **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('Aniket',age =20,city='karwar',mob=9448929883)