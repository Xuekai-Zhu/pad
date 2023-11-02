def solution():
    """There are 290 liters of oil in 24 cans. If 10 of the cans are holding 8 liters each, how much oil is each of the remaining cans holding?"""
    total_oil = 290
    total_cans = 24
    given_cans = 10
    given_cans_oil = given_cans * 8
    remaining_oil = total_oil - given_cans_oil
    remaining_cans = total_cans - given_cans
    oil_per_can = remaining_oil / remaining_cans
    result = oil_per_can
    return result

print(solution())