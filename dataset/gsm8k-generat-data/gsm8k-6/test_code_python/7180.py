def solution():
    # Calculate the number of sodas needed
    sodas_needed = 2 * 15  # every guest would drink 2 sodas

    # Calculate the number of 6 packs needed
    packs_needed = sodas_needed / 6
    if sodas_needed % 6 != 0:
        packs_needed += 1

    # Calculate the total cost
    total_cost = packs_needed * 3.00
    result = total_cost
    return result

print(solution())