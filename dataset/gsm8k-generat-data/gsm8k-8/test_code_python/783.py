def solution():
    # Define the number of parrots
    parrots = 8

    # Calculate the number of snakes
    snakes = 3 * parrots

    # Calculate the number of monkeys
    monkeys = 2 * snakes

    # Calculate the total number of parrots and snakes
    parrots_and_snakes = parrots + snakes

    # Calculate the number of elephants
    elephants = parrots_and_snakes / 2

    # Calculate the number of zebras
    zebras = elephants - 3

    # Calculate the difference between the number of zebras and monkeys
    difference = monkeys - zebras

    result = difference
    return result

print(solution())