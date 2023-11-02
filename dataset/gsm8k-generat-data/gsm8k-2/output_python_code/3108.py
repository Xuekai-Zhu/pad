def solution():
    """Lou Senior took 3 cookies out of the cookie jar and ate them.
    Since he didn't get caught by his wife, he went back the next day and took another 3 cookies out of the jar.
    But after eating just one of the cookies, he felt guilty about it and put the other two cookies back.
    His son, Louie Junior saw that his Dad was eating cookies. So, Louie Junior took seven cookies out of the jar and
    hid them in his bedroom for later.
    The next morning, Debra, Lou's wife looked into the cookie jar and reacted by accusing her husband of
    eating half of the cookies out of the cookie jar.
    How many cookies remained in the jar?"""
    initial_cookies = 16
    cookies_eaten_day1 = 3
    cookies_eaten_day2 = 2
    cookies_taken_by_louie = 7
    remaining_cookies = initial_cookies - cookies_eaten_day1 - cookies_taken_by_louie - cookies_eaten_day2
    result = remaining_cookies
    return result

print(solution())