def solution():
    cookies_per_day = 4 + 2  # Jackson's sons get a total of 6 cookies per day
    cookies_in_box = 54  # There are 54 cookies in a box

    # Calculate the number of days the box will last
    days = cookies_in_box // cookies_per_day
    result = days
    return result

print(solution())