def solution():
    # Calculate the total amount of popcorn needed
    total_popcorn = 3 + 4 + 6 + 3

    # Calculate the number of tablespoons of kernels needed for the total amount of popcorn
    tablespoons_per_cup = 2
    cups_per_tablespoon = 1 / tablespoons_per_cup
    tablespoons_needed = total_popcorn / cups_per_tablespoon

    result = tablespoons_needed
    return result

print(solution())