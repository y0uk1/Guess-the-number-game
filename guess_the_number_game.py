import random


if __name__ == '__main__':
    while True:
        min = input('Please input minimum number: ')
        max = input('Please input maximum number: ')
        if min <= max:
            break;
        else:
            print('Please follow the rule!')
            print('The minimum number must be lower than the maximum number!')

    rand = random.randint(int(min), int(max))

    while True:
        user_input = input('Please predict the random number between the minimum number and the maximum number: ')
        if int(user_input) == rand:
            print('The number you predicted is right!!')
            break
        else:
            print('Please predict the number again\n')