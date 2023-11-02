def solution():
    # Calculate number of index cards needed per day
    cards_per_day = 6 * 30 * 10

    # Calculate number of packs of cards needed
    packs_needed = cards_per_day / 50

    # Calculate total cost
    total_cost = packs_needed * 3
    result = total_cost
    return result

print(solution())