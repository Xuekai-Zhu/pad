def solution():
    """A zoo has 8 parrots. It 3 times the number of snakes than parrots and 2 times the number of monkeys than snakes. The number of elephants is half the number of parrots and snakes added up, and there are 3 fewer zebras than elephants. What is the difference in number between the zebras and the monkeys?"""
    parrots = 8
    snakes = 3 * parrots
    monkeys = 2 * snakes
    elephants = (parrots + snakes) / 2
    zebras = elephants - 3
    monkey_zebra_diff = abs(monkeys - zebras)
    result = monkey_zebra_diff
    return result

print(solution())