def solution():
    # Calculate the total number of sodas needed
    sodas_needed = 2 * 15

    # Calculate the number of 6-packs needed
    six_packs_needed = sodas_needed / 6

    # Round up to the nearest whole number
    six_packs_needed = math.ceil(six_packs_needed)

    # Calculate the total cost
    total_cost = six_packs_needed * 3.00

    result = total_cost
    return result

print(solution())