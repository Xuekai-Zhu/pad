def solution():
    """Jane sews 2 dresses a day for 7 days. Then she sews 3 dresses a day for the next 2 days. In the end, she adds 2 ribbons to each dress. How many ribbons does Jane use in total?"""
    dresses_first_week = 2 * 7
    dresses_second_week = 3 * 2
    total_dresses = dresses_first_week + dresses_second_week
    ribbons_per_dress = 2
    total_ribbons = total_dresses * ribbons_per_dress
    result = total_ribbons
    return result

print(solution())