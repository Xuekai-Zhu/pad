def solution():
    # Calculate the number of mice after one generation
    initial_mice = 8  # number of initial mice
    first_generation = initial_mice * 6  # each initial mouse has 6 pups

    # Calculate the number of mice after two generations
    second_generation = first_generation * 6  # each first generation mouse has 6 pups

    # Calculate the number of mice remaining after each mouse eats 2 of their pups
    total_lost = second_generation * 2
    total_mice = second_generation - total_lost
    result = total_mice
    return result

print(solution())