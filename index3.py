def main():
    from MyPackage.car_classes import Car

    car1 = Car('Ford', 'Mustang', 1965, 'red', 4899, 'gasoline', False)

    print(car1)


if __name__ == '__main__':
    main()
    print('main')
