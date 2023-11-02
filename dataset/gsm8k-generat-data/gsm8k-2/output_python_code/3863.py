def solution():
    """Neil baked 20 cookies. He gave 2/5 of the cookies to his friend. How many cookies are left for Neil?"""
    total_cookies = 20
    given_cookies = 2/5 * total_cookies
    remaining_cookies = total_cookies - given_cookies
    result = remaining_cookies
    return result

print(solution())