def solution():
    packs_per_day = 8 / 4  # Nedy can eat 8 packs in 4 days, so that's 2 packs per day
    total_packs = packs_per_day * 5  # Nedy eats 2 packs per day for 5 days
    friday_packs = packs_per_day * 2  # Nedy eats twice the amount on Friday, which is 4 packs
    total_packs += friday_packs  # Add Friday's packs to the total
    crackers_per_pack = 16  # Each pack has 16 crackers

    # Calculate the total number of crackers Nedy ate
    total_crackers = total_packs * crackers_per_pack
    result = total_crackers
    return result

print(solution())