def solution():
    """Ann is baking cookies. She bakes three dozen oatmeal raisin cookies, two dozen sugar cookies, and four dozen chocolate chip cookies. Ann gives away two dozen oatmeal raisin cookies, 1.5 dozen sugar cookies, and 2.5 dozen chocolate chip cookies. How many total cookies does she keep?"""
    oatmeal_raisin = 3 * 12
    sugar = 2 * 12
    chocolate_chip = 4 * 12
    oatmeal_raisin_given = 2 * 12
    sugar_given = 1.5 * 12
    chocolate_chip_given = 2.5 * 12
    total_cookies = oatmeal_raisin + sugar + chocolate_chip - oatmeal_raisin_given - sugar_given - chocolate_chip_given
    result = total_cookies
    return result

print(solution())