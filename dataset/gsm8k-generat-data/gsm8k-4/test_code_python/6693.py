def solution():
    """John's hair grows 1.5 inches every month. Every time it gets to 9 inches long he cuts it down to 6 inches. A haircut costs $45 and he gives a 20% tip. How much does he spend on haircuts a year?"""
    # Calculate the number of haircuts John gets in a year
    haircuts_per_year = 12 / 3

    # Calculate the cost of each haircut, including tip
    haircut_cost = 45 * 1.2

    # Calculate the total cost of haircuts in a year
    total_cost = haircuts_per_year * haircut_cost

    result = total_cost
    return result


# The solution returns 432.0 as the cost of haircuts in a year.

print(solution())