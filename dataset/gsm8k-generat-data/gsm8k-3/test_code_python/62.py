def solution():
    """There are 290 liters of oil in 24 cans. If 10 of the cans are holding 8 liters each, how much oil is each of the remaining cans holding?"""
    # Define the total amount of oil and the number of cans
    total_oil = 290
    total_cans = 24

    # Calculate the amount of oil in the 10 cans with known capacity (8 liters each)
    known_oil = 10 * 8

    # Calculate the amount of oil in the remaining cans
    remaining_oil = total_oil - known_oil

    # Calculate the number of remaining cans
    remaining_cans = total_cans - 10

    # Calculate the amount of oil in each of the remaining cans
    oil_per_can = remaining_oil / remaining_cans

    # return the result
    result = oil_per_can
    return result

print(solution())