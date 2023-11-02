def solution():
    num_bathrooms = 6
    rolls_per_day = 1
    num_days = 7
    num_weeks = 4
    rolls_per_pack = 12

    # Calculate the total number of rolls of toilet paper needed
    total_rolls_needed = num_bathrooms * rolls_per_day * num_days * num_weeks

    # Calculate the total number of packs of toilet paper needed
    total_packs_needed = total_rolls_needed // rolls_per_pack
    if total_rolls_needed % rolls_per_pack != 0:
        total_packs_needed += 1

    result = total_packs_needed
    return result

print(solution())