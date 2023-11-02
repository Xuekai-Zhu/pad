def solution():
    money_needed = 120
    muffin_price = 2
    muffins_per_pack = 4
    packs_per_case = 3
    
    # Calculate the total number of muffins needed to raise the money
    total_muffins_needed = money_needed / muffin_price

    # Calculate the total number of packs needed
    total_packs_needed = total_muffins_needed / muffins_per_pack

    # Calculate the total number of cases needed
    total_cases_needed = total_packs_needed / packs_per_case
    result = total_cases_needed
    return result

print(solution())