

class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest

    def value_after(self, n):
        valueAfter = int(self.principal) * ((1 + (int(self.interest)/100)) ** int(n))
        return str(valueAfter)

    def __str__(self):
        return 'Principal -  '+ format(self.principal) + ', Interest rate - ' + format(self.interest) + '%'
        #print('Principal - ', self.principal , ', Interest rate - ', self.interest,'%')

amount = Investment(eval(input('Enter the principal: ')), eval(input('Enter the interest rate: ')))
value = amount.value_after(int(input('enter the year: ')))
outp = amount.__str__()
print(outp)
print('The value is ' + value)