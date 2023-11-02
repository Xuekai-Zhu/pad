def solution():
    """Carolyn counts 6 monkeys and 6 birds in the tree outside her window. Then two of the monkeys each eat one bird. What percent of the animals outside her window are monkeys now?"""
    initial_monkeys = 6
    initial_birds = 6
    monkeys_after_eating = initial_monkeys + 2
    birds_after_eating = initial_birds - 2
    total_animals = monkeys_after_eating + birds_after_eating
    monkey_percentage = (monkeys_after_eating / total_animals) * 100
    result = monkey_percentage
    return result

print(solution())