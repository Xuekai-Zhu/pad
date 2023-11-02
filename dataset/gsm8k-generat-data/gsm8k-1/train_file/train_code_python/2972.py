def solution():
    """Jean has 60 stuffies. She keeps 1/3 of them and then gives away the rest. She gives 1/4 of what she gave away to her sister Janet. How many stuffies did Janet get?"""
    total_stuffies = 60
    kept_stuffies = total_stuffies // 3
    given_stuffies = total_stuffies - kept_stuffies
    janet_stuffies = given_stuffies // 4
    result = janet_stuffies
    return result

print(solution())