def solution():
    # Calculate the total number of chairs in the office canteen
    round_table_chairs = 2 * 6  # Each round table has 6 chairs
    rectangular_table_chairs = 2 * 7  # Each rectangular table has 7 chairs
    total_chairs = round_table_chairs + rectangular_table_chairs

    result = total_chairs
    return result

print(solution())