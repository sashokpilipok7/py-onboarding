def square(size):
    for row in range(size):
        if row == 0 or row == size - 1:
            print('🧱' * size)
        else:
            print('🧱' + '⚽' * (size - 2) + '🧱')


size = int(input('Input: '))
square(size)
