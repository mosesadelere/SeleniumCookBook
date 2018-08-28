

class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = int(amount)
        self.price = int(price)

    def get_price(self, no_of_item):
        if int(no_of_item) > int(self.amount):
            print('Please! we do not have that much in stock!')
        elif int(no_of_item) in range(0, 10):
            return self.price * int(no_of_item)
        elif no_of_item in range(10, 100):
            return (self.price*int(no_of_item)) - (0.1*self.price*int(no_of_item))
        else:
            return (self.price*int(no_of_item)) - (0.2*self.price*int(no_of_item))

    def make_purchase(self, no_of_item):
        total = self.get_price(no_of_item)
        print('Total price is ',total)


while True:
    name = input('Name of product: ')
    if name == '':
        break
    else:
        buying = Product(
        name,
        input('Amount in stock: '),
        input('Product price: ')
        )

        buying.make_purchase(input('Number of items: '))
    

    
