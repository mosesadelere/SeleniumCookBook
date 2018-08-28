import pprint
from collections import OrderedDict

favourite_language = OrderedDict()

favourite_language['jen'] = 'python'
favourite_language['sarah'] = 'c'
favourite_language['edward'] = 'ruby'
favourite_language['phil'] = 'python'

for name, language in favourite_language.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")

people = {
            'alist' : ['Moses', 'male', 34],
            'blist' : ['Aramide', 'female', 31],
            'clist' : ['Busayo', 'female', 34],
         }

days = {'January':31, 'February':28, 'March':31, 'April':30,
'May':31, 'June':30, 'July':31, 'August':31,
'September':30, 'October':31, 'November':30, 'December':31}
for v in days.values():
    pprint.pprint(v)


d = {
     'DOG' : 'has a tail and goes woof!',
     'CAT' : 'says meow',
     'MOUSE' : 'chased by cats',
     'dog' : 'has a tail and goes woof!',
     'cat' : 'says meow',
     'mouse' : 'chased by cats',
     }

points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10,
 'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2,
 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1,
 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1,
 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

word = input('Enter a word: ')
#print(d[word])

try:
    print(d[word])
except KeyError:
    print('Keys not in dictionary')
    print('Why not try it in capital letters.')
else:
    total = sum([points[k] for k in word])
    print(total)





for group, datasets in people.items():
    print("\n" + group.title() + ":")
    for dataset in datasets:
        print(dataset)

birthdays = {'Aramide' : 'Sept 17', 'Busayo' : 'Jan 5'}

while True:
    name = input('Enter a name, (a blank to quit): ')
    #name = name.title

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    elif name.__eq__(''):
        break
    else:
        print(name + ' is not in database')
        bparty = input('enter your birthday: ')
        birthdays[name] = bparty
        print('Database has been updated!!')