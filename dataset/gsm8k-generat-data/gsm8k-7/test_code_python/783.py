def solution():
    num_parrots = 8
    num_snakes = 3 * num_parrots
    num_monkeys = 2 * num_snakes
    num_elephants = (num_parrots + num_snakes) / 2
    num_zebras = num_elephants - 3

    # Calculate the difference in number between the zebras and the monkeys
    diff_zebra_monkey = num_zebras - num_monkeys
    result = diff_zebra_monkey
    return result

print(solution())