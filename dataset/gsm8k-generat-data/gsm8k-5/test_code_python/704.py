def solution():
    # Sabrina gave 10 cookies to her brother
    sabrina_cookies = 20 - 10

    # Sabrina's mother gave her half the number of cookies she gave her brother
    mother_cookies = 10 / 2
    sabrina_cookies += mother_cookies

    # Sabrina gave two-thirds of her cookies to her sister
    sister_cookies = sabrina_cookies * (2 / 3)
    sabrina_cookies -= sister_cookies

    result = sabrina_cookies
    return result

print(solution())