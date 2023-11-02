def solution():
    """Jean has 60 stuffies. She keeps 1/3 of them and then gives away the rest. She gives 1/4 of what she gave away to her sister Janet. How many stuffies did Janet get?"""
    total_stuffies = 60
    keep_percent = 1/3
    keep_count = total_stuffies * keep_percent
    give_away_count = total_stuffies - keep_count
    janet_count = give_away_count * (1/4)
    result = janet_count
    return result

print(solution())