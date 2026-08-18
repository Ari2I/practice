def first_ex():
    while True:
        char = input()
        try:
            char = int(char)
            return 10 / char
        except ArithmeticError:
            print(f'деление на {char} невозможно')
        except ValueError:
            print(f'ввод должен быть числом')


print(first_ex())
