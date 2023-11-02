def solution():
    """Jackson's oldest son gets 4 cookies after school and his youngest son gets 2 cookies after school. If there are 54 cookies in a box, how many days will the box last?"""
    oldest_son_cookies = 4
    youngest_son_cookies = 2
    total_cookies_per_day = oldest_son_cookies + youngest_son_cookies
    cookies_per_box = 54
    days_per_box = cookies_per_box // total_cookies_per_day
    result = days_per_box
    return result

print(solution())