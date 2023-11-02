def solution():
    """Sabrina gave 10 cookies to her brother. Her mother gave Sabrina half the number of cookies she gave her brother. Then Sabrina gave two-thirds of her cookies to her sister. If Sabrina had 20 cookies at the start, how many cookies are left with her?"""
    # Define the initial number of cookies
    initial_cookies = 20

    # Sabrina gave 10 cookies to her brother
    remaining_cookies = initial_cookies - 10

    # Sabrina's mother gave her half the number of cookies she gave her brother
    mother_cookies = 10 / 2
    remaining_cookies += mother_cookies

    # Sabrina gave two-thirds of her cookies to her sister
    sister_cookies = remaining_cookies * 2 / 3
    remaining_cookies -= sister_cookies

    # Return the number of cookies left with Sabrina
    result = remaining_cookies
    return result

print(solution())