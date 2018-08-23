with open('pi_millions.txt') as file_object:
    content = file_object.readlines()

print("This is SSSSSSS")
pi_number = ''
for s in content:
    pi_number += s.strip()
#print(pi_number)

birthday = input("Enter your birthday, format:ddmmyyyy: ")
if birthday in pi_number:
    print("Hurray! Your birthday appears in the first million digits of PI!")
else:
    print("wooooo! Your birthday does not appear in the first million digits of PI")
#filename = 'pi_digits.txt'
# print("This is another")
# #with open(filename) as f:

# for line in content:
#     print(line)

