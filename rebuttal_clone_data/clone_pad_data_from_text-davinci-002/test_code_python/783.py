def solution():
    parrots = 8
    snakes = 3 * parrots
    monkeys = 2 * snakes
    elephants = (parrots + snakes) / 2
    zebras = elephants - 3
    difference = zebras - monkeys
    result = difference
    return result

print(solution())