def solution():
    """Ann is baking cookies. She bakes three dozen oatmeal raisin cookies, two dozen sugar cookies, and four dozen chocolate chip cookies. Ann gives away two dozen oatmeal raisin cookies, 1.5 dozen sugar cookies, and 2.5 dozen chocolate chip cookies. How many total cookies does she keep?"""
    bake_oatmeal = 3
    bake_sugar = 2
    bake_chocolate = 4
    give_away_oatmeal = 2
    give_away_sugar = 1.5
    give_away_chocolate = 2.5
    total_give_away = give_away_oatmeal + give_away_sugar + give_away_chocolate
    total_baked = bake_oatmeal + bake_sugar + bake_chocolate
    total_cookies = total_baked - total_give_away
    result = total_cookies
    return result

print(solution())