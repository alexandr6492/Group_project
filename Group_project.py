import random

koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(koloda)
print('Lets play Black Jack!')
count = 0
comp = koloda.pop() * 2

while True:
    choice = input('Will you take a card? y/n - ')
    print(f'Casino have - {comp}')
    if comp > 21:
        print("You win!!!")
    if choice == 'y':
        current = koloda.pop()
        print('You got a card of value %d' % current)
        count += current
        if count > 21:
            print(f'Sorry! You lose. You have {count}')
            break
        elif count == 21:
            print('Сongrat! You have 21')
            break
        else:
            print('You have %d point' % count)
    elif choice == 'n':
        while comp < 16 and comp < count:
            comp += koloda.pop()
        if comp > count and comp <= 21:
            print(f"You lose. Casino have {comp}")
        elif count > comp:
            print("You win!!")
        break
