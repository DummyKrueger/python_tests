from MyPackage.car_classes import Car


def main():
    car1 = Car('Ford', 'Mustang', 1960, 'red', 4899, 'gasoline', False)

    try:
        if car1.year < 1950:
            raise NameError

        elif car1.supercharged:
            raise TypeError

        else:
            print(car1)

    except NameError:
        print(NameError)

    except:
        print('ERROR!')

    else:
        print('No errors')

    finally:
        print('end')


if __name__ == '__main__':
    print('main\n')
    main()
