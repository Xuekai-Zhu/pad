def solution():
    """Carolyn counts 6 monkeys and 6 birds in the tree outside her window. Then two of the monkeys each eat one bird. What percent of the animals outside her window are monkeys now?"""
    # Define the initial number of monkeys and birds
    monkeys = 6
    birds = 6

    # Subtract 2 from the number of birds
    birds -= 2

    # Add 2 to the number of monkeys
    monkeys += 2

    # Calculate the percentage of animals that are monkeys
    total_animals = monkeys + birds
    monkey_percentage = (monkeys / total_animals) * 100

    result = monkey_percentage
    return result

print(solution())