d = {}
while True:
    product = input('enter product name: ')
    if product.__eq__(''):
        break 
    price = eval(input('enter price: '))
    d[product] = price

print(d)
while True:
    try:
        product = input('enter name of product: ')
        print('The price of ' + product + ' is ' + str(d[product]))
    except KeyError:
        print(product + " is not in the list of fruits we have")
        print('We need the price of the new fruit.')
        newPrice = input('enter the price: ')
        d[product] = newPrice
    if product.__eq__('') or newPrice.__eq__(''):
        break
        #if product not in d.items():
        