def solution():
    weeds_in_flower_bed = 11
    weeds_in_vegetable_patch = 14
    weeds_in_grass = 32
    earnings_per_weed = 6
    total_earnings = (weeds_in_flower_bed + weeds_in_vegetable_patch + (weeds_in_grass / 2)) * earnings_per_weed
    soda_cost = .99
    money_left = total_earnings - soda_cost
    result = money_left
    return result

print(solution())