def solution():
    """Davante has twice as many friends as there are days in the week. 3 of his friends are girls. How many friends does he have that are boys?"""
    days_in_week = 7
    total_friends = days_in_week * 2
    girls = 3
    boys = total_friends - girls
    result = boys
    return result

print(solution())