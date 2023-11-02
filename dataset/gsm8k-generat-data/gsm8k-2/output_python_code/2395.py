def solution():
    """Carrie is making punch. She adds 6 12-oz cans of Mountain Dew, 28 oz of ice, and a 40 oz bottle of fruit juice. How many 10 oz servings of punch does Carrie have?"""
    mountain_dew_cans = 6
    mountain_dew_can_size = 12
    ice_size = 28
    fruit_juice_size = 40
    total_size = (mountain_dew_cans * mountain_dew_can_size) + ice_size + fruit_juice_size
    total_servings = total_size / 10
    result = total_servings
    return result

print(solution())