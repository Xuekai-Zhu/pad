def solution():
    bedroom_bulbs = 2
    bathroom_bulbs = 1
    kitchen_bulbs = 1
    basement_bulbs = 4

    # Calculate total number of bulbs needed
    total_bulbs = bedroom_bulbs + bathroom_bulbs + kitchen_bulbs + basement_bulbs

    # Add 1/2 of total_bulbs for garage
    total_bulbs += total_bulbs / 2

    # Calculate number of packs needed (2 bulbs per pack)
    packs_needed = total_bulbs // 2

    result = packs_needed
    return result

print(solution())