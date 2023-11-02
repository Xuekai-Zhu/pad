def solution():
    """There are 50 deer in a field. 50 percent of them are bucks. 20 percent of the bucks are 8 points. How many 8 point bucks are there?"""
    total_deer = 50
    bucks_percent = 50
    bucks_count = total_deer * (bucks_percent / 100)
    eight_point_percent = 20
    eight_point_count = bucks_count * (eight_point_percent / 100)
    result = eight_point_count
    return result

print(solution())