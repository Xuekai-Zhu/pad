def solution():
    """Ann is baking cookies. She bakes three dozen oatmeal raisin cookies, two dozen sugar cookies, and four dozen chocolate chip cookies. Ann gives away two dozen oatmeal raisin cookies,
    1.5 dozen sugar cookies, and 2.5 dozen chocolate chip cookies. How many total cookies does she keep?"""
    oatmeal_raisin_cookies = 3*12 - 2*12
    sugar_cookies = 2*12 - 1.5*12
    chocolate_chip_cookies = 4*12 - 2.5*12
    total_cookies = oatmeal_raisin_cookies + sugar_cookies + chocolate_chip_cookies
    result = total_cookies
    return result

print(solution())