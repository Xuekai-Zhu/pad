def solution():
    # Let's assume the number of phone chargers is x
    x = 0

    # We know that Anna has 5 times more laptop chargers than phone chargers
    laptop_chargers = 5 * x

    # We also know that the total number of chargers is 24
    total_chargers = x + laptop_chargers

    # We can set up an equation to solve for x
    x + 5x = 24
    6x = 24
    x = 4

    # Therefore, Anna has 4 phone chargers
    result = 4
    return result

print(solution())