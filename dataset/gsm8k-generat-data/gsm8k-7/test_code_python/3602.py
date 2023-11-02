def solution():
    oldest_son_cookies = 4
    youngest_son_cookies = 2
    num_cookies_in_box = 54

    # Calculate the total number of cookies eaten per day
    total_cookies_per_day = oldest_son_cookies + youngest_son_cookies

    # Calculate the number of days the box will last
    num_days = num_cookies_in_box / total_cookies_per_day
    result = num_days
    return result

print(solution())