def solution():
    """Sabrina gave 10 cookies to her brother. Her mother gave Sabrina half the number of cookies she gave her brother. Then Sabrina gave two-thirds of her cookies to her sister. If Sabrina had 20 cookies at the start, how many cookies are left with her?"""
    brother_cookies = 10
    mother_cookies = brother_cookies * 2
    sabrina_cookies = 20 - brother_cookies - mother_cookies
    sister_cookies = sabrina_cookies * (2/3)
    left_cookies = sabrina_cookies - sister_cookies
    result = left_cookies
    return result

print(solution())