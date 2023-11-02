def solution():
    initial_monkeys = 6
    initial_birds = 6
    birds_eaten = 2
    final_monkeys = initial_monkeys - birds_eaten
    final_ animals = final_monkeys + initial_birds
    percent_monkeys = (final_monkeys / final_animals) * 100
    result = percent_monkeys
    return result

print(solution())