def solution():
    # Calculate the amount of berries Martin eats in 30 days
    berries_per_day = 1/2  # in cups
    total_beries = berries_per_day * 30  # in cups

    # Calculate the number of berry packs needed to get the total amount of berries
    packs_needed = total_beries // 1 + (total_beries % 1 > 0)  # round up to the nearest pack

    # Calculate the total cost of the berry packs
    cost_per_pack = 2.00
    total_cost = cost_per_pack * packs_needed

    result = total_cost
    return result

print(solution())