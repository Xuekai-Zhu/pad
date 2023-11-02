def solution():
    desired_cookies = 10 * 24
    chocolate_chip_recipe = 4 * 12
    oatmeal_raisin_recipe = 4 * 12
    chocolate_chip_cookies = 2 * chocolate_chip_recipe
    oatmeal_raisin_cookies = 1 * oatmeal_raisin_recipe
    cookies_made = chocolate_chip_cookies + oatmeal_raisin_cookies
    cookies_needed = desired_cookies - cookies_made
    recipe_ratio = chocolate_chip_recipe / oatmeal_raisin_recipe
    desired_chocolate_chip_cookies = cookies_needed * recipe_ratio
    desired_chocolate_chip_batches = desired_chocolate_chip_cookies / chocolate_chip_recipe
    result = desired_chocolate_chip_batches
    return result

print(solution())