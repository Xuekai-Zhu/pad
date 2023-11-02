def solution():
    """Out of the 200 cookies that Javier baked from the recipe he learned online, his wife took 30%, and his daughter took 40 from the remaining cookies. If he ate half of the remaining cookies, how many cookies did they not eat?"""
    total_cookies = 200
    wife_cookies = int(total_cookies * 0.3)
    remaining_cookies = total_cookies - wife_cookies - 40
    javier_cookies = int(remaining_cookies / 2)
    not_eaten_cookies = remaining_cookies - javier_cookies
    result = not_eaten_cookies
    return result

print(solution())