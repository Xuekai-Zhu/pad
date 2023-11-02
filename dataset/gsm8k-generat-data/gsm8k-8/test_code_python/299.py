def solution():
    # Calculate the total number of cookies Basil gets in a day
    daily_cookies = (1/2) + (1/2) + 2

    # Calculate the total number of cookies needed for 30 days
    total_cookies = 30 * daily_cookies

    # Calculate the number of boxes needed, rounding up to the nearest whole number
    boxes_needed = math.ceil(total_cookies / 45)

    result = boxes_needed
    return result

print(solution())