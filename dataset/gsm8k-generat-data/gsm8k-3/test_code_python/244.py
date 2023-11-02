def solution():
    """Ann is baking cookies. She bakes three dozen oatmeal raisin cookies, two dozen sugar cookies, and four dozen chocolate chip cookies. Ann gives away two dozen oatmeal raisin cookies, 1.5 dozen sugar cookies, and 2.5 dozen chocolate chip cookies. How many total cookies does she keep?"""
    # Define the number of cookies per dozen for each type of cookie
    OATMEAL_RAISIN_COOKIES_PER_DOZEN = 12
    SUGAR_COOKIES_PER_DOZEN = 12
    CHOCOLATE_CHIP_COOKIES_PER_DOZEN = 12

    # Define the number of dozens of each type of cookie Ann bakes and gives away
    oatmeal_raisin_bake = 3
    oatmeal_raisin_give_away = 2
    sugar_bake = 2
    sugar_give_away = 1.5
    chocolate_chip_bake = 4
    chocolate_chip_give_away = 2.5

    # Calculate the total number of cookies Ann bakes
    total_bake = (oatmeal_raisin_bake * OATMEAL_RAISIN_COOKIES_PER_DOZEN) + (sugar_bake * SUGAR_COOKIES_PER_DOZEN) + (
            chocolate_chip_bake * CHOCOLATE_CHIP_COOKIES_PER_DOZEN)

    # Calculate the total number of cookies Ann gives away
    total_give_away = (oatmeal_raisin_give_away * OATMEAL_RAISIN_COOKIES_PER_DOZEN) + (
            sugar_give_away * SUGAR_COOKIES_PER_DOZEN) + (
                             chocolate_chip_give_away * CHOCOLATE_CHIP_COOKIES_PER_DOZEN)

    # Calculate the total number of cookies that Ann keeps
    total_cookies = total_bake - total_give_away

    # Display the total number of cookies
    result = total_cookies
    return result

print(solution())