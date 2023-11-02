def solution():
    """Carolyn counts 6 monkeys and 6 birds in the tree outside her window. Then two of the monkeys each eat one bird. What percent of the animals outside her window are monkeys now?"""
    # Define the initial number of monkeys and birds
    monkeys = 6
    birds = 6

    # Subtract 2 birds that were eaten by monkeys
    birds -= 2

    # Calculate the new total number of animals
    total_animals = monkeys + birds

    # Calculate the percentage of animals that are now monkeys
    monkey_percent = (monkeys / total_animals) * 100

    # Display the percentage of animals that are now monkeys
    result = monkey_percent
    return result

print(solution())