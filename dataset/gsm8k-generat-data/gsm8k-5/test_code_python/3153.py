def solution():
    initial_monkeys = 6
    initial_birds = 6
    monkeys_after_eating = initial_monkeys + 2  # Two of the monkeys ate one bird each
    birds_after_eating = initial_birds - 2  # Two of the birds were eaten by the monkeys
    total_animals = monkeys_after_eating + birds_after_eating

    # Calculate the percentage of animals that are monkeys
    percent_monkeys = (monkeys_after_eating / total_animals) * 100
    result = percent_monkeys
    return result

print(solution())