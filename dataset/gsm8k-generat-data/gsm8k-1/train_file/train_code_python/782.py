def solution():
    """A zoo has 8 parrots. It 3 times the number of snakes than parrots and 2 times the number of monkeys than snakes. The number of elephants is half the number of parrots and snakes added up, and there are 3 fewer zebras than elephants. What is the difference in number between the zebras and the monkeys?"""
    num_parrots = 8
    num_snakes = num_parrots * 3
    num_monkeys = num_snakes * 2
    num_elephants = (num_parrots + num_snakes) / 2
    num_zebras = num_elephants - 3
    num_difference = num_zebras - num_monkeys
    result = abs(num_difference)  # taking absolute value in case they are negative
    
    return result

print(solution())