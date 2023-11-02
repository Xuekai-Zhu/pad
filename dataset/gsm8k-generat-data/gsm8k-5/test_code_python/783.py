def solution():
    # Calculate the number of snakes
    parrots = 8
    snakes = 3 * parrots 

    # Calculate the number of monkeys
    monkeys = 2 * snakes 

    # Calculate the number of elephants
    elephants = (parrots + snakes) / 2

    # Calculate the number of zebras
    zebras = elephants - 3

    # Calculate the difference between zebras and monkeys
    difference = monkeys - zebras

    result = difference
    return result

print(solution())