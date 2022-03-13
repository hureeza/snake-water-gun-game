import random

def game(comp,you):
    if comp == 'You':
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True

    elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False

    elif comp == "g":
        if you == "s":
            return False
        elif you == 'w':
            return True

print("comp turn: snake (s) water (w) or gun(g)?")
random_number = random.randint(1,3)
if random_number == 1:
    comp = 's' 
elif random_number == 2:
    comp = 'w'
elif random_number == 3:
    comp = 'g'

you = input("your turn: snake (s), water (w) or gun(g)?")
x = game(comp, you)

if x == None:
    print("Game is a tie")
elif x:
    print("you win")
else:
    print("lose")