def solution():
    """Carrie is making punch. She adds 6 12-oz cans of Mountain Dew, 28 oz of ice, and a 40 oz bottle of fruit juice. How many 10 oz servings of punch does Carrie have?"""
    mountain_dew_cans = 6
    mountain_dew_ounces = mountain_dew_cans * 12
    ice_ounces = 28
    fruit_juice_ounces = 40
    total_ounces = mountain_dew_ounces + ice_ounces + fruit_juice_ounces
    servings = total_ounces // 10
    result = servings
    return result

print(solution())