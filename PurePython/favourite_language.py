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

for group, datasets in people.items():
    print("\n" + group.title() + ":")
    for dataset in datasets:
        print(dataset)