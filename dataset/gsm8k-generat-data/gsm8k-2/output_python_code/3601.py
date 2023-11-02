def solution():
    """Jackson's oldest son gets 4 cookies after school and his youngest son gets 2 cookies after school. If there are 54 cookies in a box, how many days will the box last?"""
    num_cookies_per_day = 4 + 2
    num_cookies_in_box = 54
    num_days = num_cookies_in_box / num_cookies_per_day
    result = num_days
    return result

print(solution())