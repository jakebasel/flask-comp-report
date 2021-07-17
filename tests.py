from data import data

# list of dictionaries
products = data

def test1():
    print("***Printing each product title")

    for prod in products:
        print(prod["title"])

# test 2
# print sum of all prices
def test2():
    print("-- sum of all prices")
    sum = 0
    for prod in products:
        price = prod["price"]
        sum += price
    print(f"The sum is: {sum}")

def test3():
    print("Products with prices over $13")

    for prod in products:
        if(prod["price"]>13):
            print(prod["title"])

def test4():
    print("--- total stock value")

    sum = 0
    for prod in products:
        valu = prod["price"] * prod["stock"]
        sum += valu

    print(f"The value of the stock is {sum}")

def test5():
    print("** unique categories")

    unique_categories = []
    for prod in products:
        cat = prod["category"]

        if cat not in unique_categories:
            unique_categories.append(cat)
            print(cat)

def run_tests():
    print("Starting tests")
    test1()
    test2()
    test3()
    test4()
    

run_tests()


