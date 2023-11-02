def solution():
    
    mountain_dew_cans = 6
    mountain_dew_ounces = mountain_dew_cans * 12
    ice_ounces = 28
    fruit_juice_ounces = 40
    total_ounces = mountain_dew_ounces + ice_ounces + fruit_juice_ounces
    servings = total_ounces // 10
    result = servings
    return result

print(solution())