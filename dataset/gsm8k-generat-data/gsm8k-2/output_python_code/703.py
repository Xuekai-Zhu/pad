def solution():
    """Sabrina gave 10 cookies to her brother. Her mother gave Sabrina half the number of cookies she gave her brother.
    Then Sabrina gave two-thirds of her cookies to her sister. If Sabrina had 20 cookies at the start, how many cookies
    are left with her?"""
    brother_cookies = 10
    mother_cookies = brother_cookies * 2
    sabrina_cookies = 20
    sabrina_cookies += mother_cookies // 2  
    sabrina_cookies = int(sabrina_cookies * (1/3))  
    remaining_cookies = sabrina_cookies
    result = remaining_cookies
    return result

print(solution())