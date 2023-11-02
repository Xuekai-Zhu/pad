def solution():
    """Jen bought a bag of cookies and ate three-quarters of the bag that day. The next day, she ate half of the remaining cookies. She has 8 cookies left on the third day. How many cookies were in the bag to start?"""
    # Assume that there were x cookies in the bag to start

    # Calculate the number of cookies remaining after the first day
    first_day_cookies = x * 0.25
    remaining_cookies = x - first_day_cookies

    # Calculate the number of cookies remaining after the second day
    second_day_cookies = remaining_cookies * 0.5
    remaining_cookies -= second_day_cookies

    # At this point, there are 8 cookies left, so we can solve for x
    remaining_cookies = 8
    x = remaining_cookies / (1 - 0.25 - 0.5)

    result = round(x)
    return result

print(solution())