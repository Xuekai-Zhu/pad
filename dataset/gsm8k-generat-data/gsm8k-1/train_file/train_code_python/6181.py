def solution():
    """Alan counted how many chairs the office canteen has. It has 2 round tables and 2 rectangular tables. Each round table has 6 chairs, and each rectangular table has 7 chairs. How many chairs are there in all?"""
    round_tables = 2
    rect_tables = 2
    chairs_per_round_table = 6
    chairs_per_rect_table = 7
    total_chairs = (round_tables * chairs_per_round_table) + (rect_tables * chairs_per_rect_table)
    result = total_chairs
    return result

print(solution())