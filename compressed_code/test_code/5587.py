def solution():
    
    money_needed = 120
    muffin_price = 2
    muffins_per_pack = 4
    packs_per_case = 3
    muffins_per_case = packs_per_case * muffins_per_pack
    cases_needed = money_needed / (muffins_per_case * muffin_price)
    result = cases_needed
    return result

print(solution())