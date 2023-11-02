def solution():
    num_rolls = 12
    num_children = 6
    num_rolls_per_child = 1
    num_pieces_per_roll = 8

    # Calculate the total number of rolls Mrs. Sherman made
    total_rolls = num_rolls * num_children

    # Calculate the number of pieces of rolls Mrs. Sherman broke
    num_broken_rolls = (num_rolls - num_rolls_per_child) * num_pieces_per_roll

    # Calculate the number of pieces of rolls Mrs. Sherman fed to the chickens
    num_chickens_rolls = num_broken_rolls * num_pieces_per_roll
    result = num_chickens_rolls
    return result

print(solution())