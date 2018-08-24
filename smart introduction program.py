g=input('Enter your gender as m or f ')
if( (g=='m' or g=='f')and g.isalpha()):
    if g=='m':
        name=input('Enter your name:')
        if(name.isalpha()):
            print('Hello {},sir'.format(name))
        else:
            print('Invalid name')
        age=input('Enter the age:')
        if(age.isdigit()):
            age=int(age)
            if (age>20):
                print('You are able to enroll for python fundamental course\n')
            else:
                print('yOur age is below  so u cant enroll')

    elif g=='f':
        name=input('Enter your name:')
        if(name.isalpha()):
            print('Hello {},mam'.format(name))
        else:
            print('Invalid name')
        age=input('Enter the age:')
        if(age.isdigit()):
            age=int(age)
            if (age>19):
                print('You are able to enroll for core java course\n')
            else:
                print('yOur age is below than our avg so u cant enroll')

else:
    print('Invalid gender')
