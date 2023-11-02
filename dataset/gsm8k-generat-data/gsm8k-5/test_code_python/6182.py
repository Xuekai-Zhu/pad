def solution():
    # Calculate the total number of chairs in the round tables
    total_chairs_round_tables = 2 * 6  # 2 round tables, each with 6 chairs

    # Calculate the total number of chairs in the rectangular tables
    total_chairs_rectangular_tables = 2 * 7  # 2 rectangular tables, each with 7 chairs

    # Calculate the total number of chairs in the office canteen
    total_chairs = total_chairs_round_tables + total_chairs_rectangular_tables
    result = total_chairs
    return result

print(solution())