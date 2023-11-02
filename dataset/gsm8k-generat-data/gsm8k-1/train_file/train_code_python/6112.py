def solution():
    """Jackson is buying chairs for his restaurant. He has 6 tables with 4 seats and 12 tables with 6 seats. How many chairs total does Jackson need to buy?"""
    tables_4_seats = 6
    tables_6_seats = 12
    chairs_4_seats = tables_4_seats * 4
    chairs_6_seats = tables_6_seats * 6
    total_chairs = chairs_4_seats + chairs_6_seats
    result = total_chairs
    return result

print(solution())