We will first find the number of each animal in the zoo.

def solution():
    # Find the number of each animal in the zoo
    parrots = 8
    snakes = 3 * parrots
    monkeys = 2 * snakes
    elephants = (parrots + snakes) / 2
    zebras = elephants - 3
    
    # Find the difference between the number of zebras and monkeys
    diff = abs(zebras - monkeys)
    result = diff
    return result

print(solution())