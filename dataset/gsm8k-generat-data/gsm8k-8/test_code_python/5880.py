def solution():
    # Calculate the total packs of crackers that Nedy ate from Monday to Thursday
    total_packs_mon_thurs = 8 * 4

    # Calculate the total packs of crackers that Nedy ate on Friday
    friday_eats = 8 * 2

    # Calculate the total packs of crackers that Nedy ate in all
    total_eats = total_packs_mon_thurs + friday_eats
    crackers_eaten = total_eats * 6  # Each pack has 6 crackers
    result = crackers_eaten
    return result

print(solution())