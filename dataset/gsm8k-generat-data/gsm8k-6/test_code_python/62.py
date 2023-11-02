def solution():
    # Calculate the total amount of oil in the 10 cans holding 8 liters each
    total_oil_10_cans = 10 * 8

    # Calculate the amount of oil in the remaining cans
    remaining_cans = 24 - 10
    remaining_oil = 290 - total_oil_10_cans

    # Calculate the amount of oil each of the remaining cans is holding
    oil_per_can = remaining_oil / remaining_cans
    result = oil_per_can
    return result

print(solution())