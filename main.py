from minus import minus
from plus import plus
def main():
    znak = input(f'{chr(3)} Что хотите прибавить или убавить? НАПИШИТЕ +/-: ')
    try:
        num1 = float(input(f'{chr(3)} Введите первое число: '))
        num2 = float(input(f'{chr(3)} Введите второе число: '))
        print(
            '------Третьего не дано, бери что дают, и не вякай! Иш шо удумал. Думаешь ради тебя буду делать код больше и сложнее, не братан или братанка так не пойдет!------')
        if znak == '+':
            print(plus(num1, num2))
        elif znak == '-':
            print(minus(num1, num2))
        else:
            print('Неправильно ввел значение!')
    except:
        print('Цифры нужно ввводить, а не то что ты ввел')

if __name__ == '__main__':
    main()
