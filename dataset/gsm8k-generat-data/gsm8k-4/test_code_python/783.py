def solution():
    """A zoo has 8 parrots. It 3 times the number of snakes than parrots and 2 times the number of monkeys than snakes. The number of elephants is half the number of parrots and snakes added up, and there are 3 fewer zebras than elephants. What is the difference in number between the zebras and the monkeys?"""
    # Define the number of parrots
    parrots = 8

    # Calculate the number of snakes
    snakes = parrots * 3

    # Calculate the number of monkeys
    monkeys = snakes * 2

    # Calculate the number of elephants
    elephants = (parrots + snakes) / 2

    # Calculate the number of zebras
    zebras = elephants - 3

    # Calculate the difference between the number of zebras and monkeys
    difference = abs(zebras - monkeys)

    result = difference
    return result

print(solution())