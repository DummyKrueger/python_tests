def iterable_converter(some_string):
    for letter in some_string:
        yield letter


def main():
    iterable_string = iterable_converter(input('Type something: '))

    while True:
        answer = input('Output? (y/n)')

        if answer == 'n':
            break

        elif answer != 'y':
            continue

        else:
            print(next(iterable_string))


if __name__ == '__main__':
    main()
