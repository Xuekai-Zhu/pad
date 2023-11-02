def solution():
    """Jen bought a bag of cookies and ate three-quarters of the bag that day. The next day, she ate half of the remaining cookies. She has 8 cookies left on the third day. How many cookies were in the bag to start?"""
    cookies_left_third_day = 8
    remaining_after_day_two = cookies_left_third_day * 2
    initial_cookies = remaining_after_day_two * 4
    result = initial_cookies
    return result

print(solution())