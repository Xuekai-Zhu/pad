def solution():
    # Calculate the initial number of legs of furniture
    num_chair_legs = 80 * 5  # 80 office chairs with 5 legs each
    num_table_legs = 20 * 3  # 20 round tables with 3 legs each
    total_legs = num_chair_legs + num_table_legs  # total number of legs of furniture

    # Calculate the number of legs of furniture remaining after 40% of chairs are disposed of
    num_damaged_chairs = 0.4 * 80  # 40% of 80 chairs are damaged
    num_remaining_chairs = 80 - num_damaged_chairs  # number of chairs remaining after disposing of damaged chairs
    remaining_chair_legs = num_remaining_chairs * 5  # number of legs of remaining chairs
    remaining_table_legs = 20 * 3  # number of legs of remaining tables
    total_remaining_legs = remaining_chair_legs + remaining_table_legs  # total number of legs of furniture remaining

    result = total_remaining_legs
    return result

print(solution())