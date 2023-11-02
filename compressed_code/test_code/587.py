def solution():
    
    parrots = 8
    snakes = 3 * parrots
    monkeys = 2 * snakes
    elephants = (parrots + snakes) / 2
    zebras = elephants - 3
    monkey_zebra_diff = abs(monkeys - zebras)
    result = monkey_zebra_diff
    return result

print(solution())