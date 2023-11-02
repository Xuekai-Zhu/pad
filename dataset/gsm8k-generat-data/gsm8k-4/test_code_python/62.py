def solution():
    """There are 290 liters of oil in 24 cans. If 10 of the cans are holding 8 liters each, how much oil is each of the remaining cans holding?"""
    # Define the total amount of oil and the number of cans
    total_oil = 290
    cans = 24

    # Calculate the amount of oil in the 10 cans
    oil_in_10_cans = 10 * 8

    # Calculate the amount of oil in the remaining cans
    remaining_oil = total_oil - oil_in_10_cans

    # Calculate the number of remaining cans
    remaining_cans = cans - 10

    # Calculate the amount of oil in each of the remaining cans
    oil_per_can = remaining_oil / remaining_cans

    result = oil_per_can
    return result

print(solution())