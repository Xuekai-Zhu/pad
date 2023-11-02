def solution():
    """Carolyn counts 6 monkeys and 6 birds in the tree outside her window. Then two of the monkeys each eat one bird. What percent of the animals outside her window are monkeys now?"""
    initial_monkeys = 6
    initial_birds = 6
    monkeys_eat_birds = 2
    final_monkeys = initial_monkeys + monkeys_eat_birds
    final_birds = initial_birds - monkeys_eat_birds
    total_animals = final_monkeys + final_birds
    percent_monkeys = (final_monkeys / total_animals) * 100
    result = percent_monkeys
    return result

print(solution())