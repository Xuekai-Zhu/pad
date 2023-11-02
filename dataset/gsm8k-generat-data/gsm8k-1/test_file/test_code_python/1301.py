def solution():
    """The Adams family is busy making cookies. So far, they've made 7995 cookies. They have 2595 rainbow cookies, 3075 oatmeal cookies, and some chocolate chip cookies. How many chocolate chip cookies have they made?"""
    total_cookies = 7995
    rainbow_cookies = 2595
    oatmeal_cookies = 3075
    chocolate_chip_cookies = total_cookies - rainbow_cookies - oatmeal_cookies
    result = chocolate_chip_cookies
    return result

print(solution())