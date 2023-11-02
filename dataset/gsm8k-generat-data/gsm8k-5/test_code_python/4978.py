def solution():
    row_length = 120  # Each row is 120 feet long
    space_per_seed = 0.75  # Each seed needs 0.75 feet of space (18 inches to its right)

    # Calculate the number of seeds that can be planted in each row
    num_seeds_per_row = int(row_length / space_per_seed)
    result = num_seeds_per_row
    return result

print(solution())