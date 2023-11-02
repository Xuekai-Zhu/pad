def solution():
    # Calculate the number of seeds needed to plant 20 flowers, considering half will die
    total_seeds_needed = 20 * 2

    # Calculate the number of seed packs needed, rounding up to the nearest integer
    seed_packs_needed = math.ceil(total_seeds_needed/25)

    # Calculate the total cost of seed packs needed
    total_cost = seed_packs_needed * 5

    result = total_cost
    return result

print(solution())