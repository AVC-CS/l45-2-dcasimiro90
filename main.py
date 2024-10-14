import random


def main():
    total = 0
    numbers = []
    while total <= 100:
        number = random.randint(0, 100)
        if total + number > 100:
            break
        numbers.append(number)
        total += number

    print(f'The random values are: {numbers}')
    print(f'The total is: {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
