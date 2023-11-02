def solution():
    # Calculate the number of seed packs Madeline needs to buy
    seeds_needed = 20 * 2  # assuming half of the seeds die, Madeline needs to plant 2 seeds for every 1 flower
    packs_needed = seeds_needed // 25 + 1  # round up to the nearest pack
    # Calculate the total cost
    cost = packs_needed * 5
    result = cost
    return result

print(solution())