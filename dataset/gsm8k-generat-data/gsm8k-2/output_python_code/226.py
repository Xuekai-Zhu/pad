def solution():
    """There are 32 tables in a hall. Half the tables have 2 chairs each, 5 have 3 chairs each and the rest have 4 chairs each. How many chairs in total are in the hall?"""
    total_tables = 32
    half_tables = total_tables // 2
    two_chair_tables = half_tables
    three_chair_tables = 5
    four_chair_tables = total_tables - half_tables - three_chair_tables
    total_chairs = (two_chair_tables * 2) + (three_chair_tables * 3) + (four_chair_tables * 4)
    result = total_chairs
    return result

print(solution())