def solution():
    num_round_tables = 2
    num_rect_tables = 2
    chairs_per_round_table = 6
    chairs_per_rect_table = 7

    # Calculate the total number of chairs at the round tables
    total_round_chairs = num_round_tables * chairs_per_round_table

    # Calculate the total number of chairs at the rectangular tables
    total_rect_chairs = num_rect_tables * chairs_per_rect_table

    # Calculate the total number of chairs in the canteen
    total_chairs = total_round_chairs + total_rect_chairs
    result = total_chairs
    return result

print(solution())