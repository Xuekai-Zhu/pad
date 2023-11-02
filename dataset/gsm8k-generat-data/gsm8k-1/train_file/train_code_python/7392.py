def solution():
    """There are 70 cookies in a jar. If there are only 28 cookies left after a week, and Paul took out the same amount each day, how many cookies did he take out in four days?"""
    total_cookies = 70
    cookies_left = 28
    days = 7
    cookies_per_day = (total_cookies-cookies_left) / days
    cookies_in_four_days = cookies_per_day * 4
    result = cookies_in_four_days
    return result

print(solution())