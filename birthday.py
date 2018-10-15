
birthdays = {'sandhun' : 'jun 15', 'shini' : 'may 30', 'sailakshmi' : 'jun 15'}

while True:
    print('enter the name: (blank to quit)')
    name = input()
    if name =='':
         break

    if name in birthdays:
        print(birthdays[name] + 'is the birthday of ' + name)
    else:
        print('i do not have info about for '+name)
        print('what is their birthday')
        bday = input()
        birthdays[name] = bday 
        print('birthday is updated')
