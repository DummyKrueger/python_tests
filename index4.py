def main():
    total = 0

    while True:
        try:
            num = input('\nInserisci un numero intero: ')

            if num == 'q':
                break

            else:
                num = int(num)

        except:
            print('\nNon hai inserito un numero intero!')

            continue

        else:
            total += num
            
            print(f'\n Il valore totale è {total}')


if __name__ == '__main__':
    main()
