a= 10
def something():
    global a
    a=15
    print(a)



something()
print(a)