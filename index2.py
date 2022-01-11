total = 0

while True:
    user_input = input('\nAdd a number: ')

    if (user_input != 'exit'):
        if (user_input.isdigit()):
            total += int(user_input)
            print('\nTotal is ' + str(total))

        else:
            print('\nThis is not a number!')
            user_input = input('\nTry again: ')

    else:
        break

print('\nExiting...\n')
