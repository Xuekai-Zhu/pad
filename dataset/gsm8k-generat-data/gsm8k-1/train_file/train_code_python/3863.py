def solution():
    """Neil baked 20 cookies. He gave 2/5 of the cookies to his friend. How many cookies are left for Neil?"""
    total_cookies = 20
    fraction_given = 2/5
    cookies_given = total_cookies * fraction_given
    cookies_left = total_cookies - cookies_given
    result = cookies_left
    return result

print(solution())