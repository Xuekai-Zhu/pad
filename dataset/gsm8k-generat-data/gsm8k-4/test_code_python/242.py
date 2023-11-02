def solution():
    """Ann is baking cookies. She bakes three dozen oatmeal raisin cookies, two dozen sugar cookies, and four dozen chocolate chip cookies. Ann gives away two dozen oatmeal raisin cookies, 1.5 dozen sugar cookies, and 2.5 dozen chocolate chip cookies. How many total cookies does she keep?"""
    # Define the number of cookies Ann bakes
    oatmeal_cookies_baked = 3 * 12
    sugar_cookies_baked = 2 * 12
    chocolate_cookies_baked = 4 * 12

    # Define the number of cookies Ann gives away
    oatmeal_cookies_given = 2 * 12
    sugar_cookies_given = 1.5 * 12
    chocolate_cookies_given = 2.5 * 12

    # Calculate the total number of cookies Ann keeps
    total_cookies = oatmeal_cookies_baked - oatmeal_cookies_given + sugar_cookies_baked - sugar_cookies_given + chocolate_cookies_baked - chocolate_cookies_given

    # Return the result
    result = total_cookies
    return result

print(solution())