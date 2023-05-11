koloda = [6,7,8,9,10,2,3,4,11] *4
import random
random.shuffle(koloda)
print('Lets play Black Jack!')
count = 0

while True:
    choice = input('Will you take a card? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('You got a card of value %d' %current)
        count += current
        if count > 21:
            print('Sorry! You lose')
            break
        elif count == 21:
            print('Сongrat! You have 21')
            break
        else:
            print('You have %d point' %count)
    elif choice == 'n':
        print('You have %d points and you finished game' %count)
        break
