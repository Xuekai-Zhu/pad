def solution():
    """For the school play, 40 rows of chairs were set up where there were 20 chairs in each row. If only 10 seats were not occupied, how many seats were taken?"""
    total_chairs = 40 * 20
    occupied_chairs = total_chairs - 10
    result = occupied_chairs
    return result

print(solution())