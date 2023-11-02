def solution():
    row_length = 120  # in feet
    seed_spacing = 18  # in inches
    row_width = row_length * 12  # convert row length to inches

    # Calculate the number of seeds that can fit in each row
    num_seeds_per_row = row_width // seed_spacing

    result = num_seeds_per_row
    return result

print(solution())