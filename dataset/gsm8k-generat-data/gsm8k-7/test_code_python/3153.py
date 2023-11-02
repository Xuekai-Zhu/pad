def solution():
    initial_monkeys = 6
    initial_birds = 6
    monkeys_who_ate_birds = 2
    birds_eaten = 2

    # Calculate the new number of monkeys after two eat a bird each
    monkeys_after_eating = initial_monkeys + monkeys_who_ate_birds

    # Calculate the new number of birds after two are eaten
    birds_after_eating = initial_birds - birds_eaten

    # Calculate the total number of animals now
    total_animals = monkeys_after_eating + birds_after_eating

    # Calculate the percent of animals that are now monkeys
    percent_monkeys = (monkeys_after_eating / total_animals) * 100
    result = percent_monkeys
    return result

print(solution())