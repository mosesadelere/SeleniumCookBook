import sys
filename = 'learning_python.txt'

with open(filename, 'r+') as f:
    f.writelines("I love my wife")
    content = f.readlines()
    #content.replace('wife', 'Aramide')
resevoir = ''
for line in content:
    resevoir += line

resevoir.replace('wife','Aramide')
guest = ''
while(not guest.__eq__('quit')):
    guest = input("Enter your name as Guest: ")
    
    if guest.__eq__('quit'):
            #break
            sys.exit()
    else:
        with open('guestfile.txt','a') as Guest:
            Guest.write(guest.title() + "\n")
            
        
#print("\n")