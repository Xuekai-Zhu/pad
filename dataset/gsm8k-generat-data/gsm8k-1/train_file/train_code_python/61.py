def solution():
    """There are 290 liters of oil in 24 cans. If 10 of the cans are holding 8 liters each, how much oil is each of the remaining cans holding?"""
    total_liters = 290
    total_cans = 24
    given_cans = 10
    given_liters = 8 * given_cans
    remaining_cans = total_cans - given_cans
    remaining_liters = total_liters - given_liters
    liters_per_can = remaining_liters / remaining_cans
    result = liters_per_can
    return result

print(solution())