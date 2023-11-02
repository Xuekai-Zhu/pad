def solution():
    """Jen bought a bag of cookies and ate three-quarters of the bag that day. The next day, she ate half of the remaining cookies. She has 8 cookies left on the third day. How many cookies were in the bag to start?"""
    cookies_left_day2 = 8
    cookies_left_day1 = cookies_left_day2 * 2
    cookies_start = cookies_left_day1 / 0.25
    result = cookies_start
    return result

print(solution())