import random
def birds_milk():
    monet = random.randint(1, 20)
    if monet <= 3:
        return 'yellow'
    if monet <= 10: 
        return 'black'
    return 'white'

print(birds_milk())