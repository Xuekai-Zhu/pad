def solution():
    """There are 290 liters of oil in 24 cans. If 10 of the cans are holding 8 liters each, how much oil is each of the remaining cans holding?"""
    total_oil = 290
    oil_in_8_liter_cans = 10
    oil_in_each_8_liter_can = 8
    total_oil_in_8_liter_cans = oil_in_8_liter_cans * oil_in_each_8_liter_can
    remaining_oil = total_oil - total_oil_in_8_liter_cans
    remaining_cans = 14
    oil_in_remaining_cans = remaining_oil / remaining_cans
    result = oil_in_remaining_cans
    
    return result

print(solution())