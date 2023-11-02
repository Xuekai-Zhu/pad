def solution():
    num_sandwiches = 8
    slices_per_sandwich = 2
    slices_per_pack = 4

    # Calculate the total number of slices of bread needed for all sandwiches
    total_slices = num_sandwiches * slices_per_sandwich

    # Calculate the total number of packs of bread needed
    total_packs = total_slices / slices_per_pack

    # Round up to the nearest whole number of packs
    total_packs = int(total_packs) + (total_packs % 1 > 0)

    result = total_packs
    return result

print(solution())