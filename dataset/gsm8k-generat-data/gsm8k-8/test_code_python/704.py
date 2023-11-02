def solution():
    # Sabrina gave 10 cookies to her brother
    sabrina_cookies = 20 - 10

    # Sabrina's mother gave her half the number of cookies she gave her brother
    sabrina_cookies += 10 / 2

    # Sabrina gave two-thirds of her cookies to her sister
    sabrina_cookies *= 1 / 3

    result = sabrina_cookies
    return result

print(solution())