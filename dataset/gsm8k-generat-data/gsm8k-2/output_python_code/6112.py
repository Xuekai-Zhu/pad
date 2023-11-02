def solution():
    """Jackson is buying chairs for his restaurant. He has 6 tables with 4 seats and 12 tables with 6 seats. How many chairs total does Jackson need to buy?"""
    table_1_seats = 4
    table_1_count = 6
    table_2_seats = 6
    table_2_count = 12
    total_chairs = (table_1_seats * table_1_count) + (table_2_seats * table_2_count)
    result = total_chairs
    return result

print(solution())