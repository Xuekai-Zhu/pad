def solution():
    mountain_dew_cans = 6
    mountain_dew_can_size = 12  # in ounces
    ice_size = 28  # in ounces
    fruit_juice_bottle_size = 40  # in ounces
    serving_size = 10  # in ounces

    # Calculate the total volume of all ingredients in ounces
    total_volume = (mountain_dew_cans * mountain_dew_can_size) + ice_size + fruit_juice_bottle_size

    # Calculate the total number of servings of punch
    num_servings = total_volume // serving_size
    result = num_servings
    return result

print(solution())