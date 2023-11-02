def solution():
    packs_per_day = 8
    friday_multiplier = 2
    # Calculate the total packs of crackers Nedy ate from Monday to Thursday
    total_packs_before_friday = packs_per_day * 4

    # Calculate the number of packs Nedy ate on Friday
    friday_packs = packs_per_day * friday_multiplier

    # Calculate the total packs of crackers Nedy ate in all
    total_packs = total_packs_before_friday + friday_packs
    result = total_packs
    return result

print(solution())