def solution():
    # Convert the 1.5 quart bottle to ounces
    bottle_ounces = 1.5 * 32  # 1 quart = 32 ounces, so 1.5 quarts = 48 ounces

    # Add the number of ounces in the can to the number of ounces in the bottle
    total_ounces = bottle_ounces + 12

    result = total_ounces
    return result

print(solution())