def solution():
    """Randy has 9 oatmeal cookies, 4 chocolate chip cookies, and 5 sugar cookies. He ate 3 cookies for an early day snack, one of each flavor. He ate 2 oatmeal cookies for lunch. He gives 2 sugar cookies to his friends. Then, he bakes 4 of each flavor for dinner. How many cookies does he have now?"""
    oatmeal_cookies = 9
    chocolate_chip_cookies = 4
    sugar_cookies = 5
    cookies_eaten = 6
    oatmeal_cookies_eaten = 3
    sugar_cookies_given_away = 2
    cookies_baked = 12

    total_cookies = (oatmeal_cookies + chocolate_chip_cookies + sugar_cookies) - \
        cookies_eaten - oatmeal_cookies_eaten - sugar_cookies_given_away + cookies_baked
    result = total_cookies
    return result

print(solution())