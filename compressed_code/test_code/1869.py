def solution():
    
    mountain_dew_cans = 6
    mountain_dew_can_size = 12
    ice_size = 28
    fruit_juice_size = 40
    total_size = (mountain_dew_cans * mountain_dew_can_size) + ice_size + fruit_juice_size
    total_servings = total_size / 10
    result = total_servings
    return result

print(solution())