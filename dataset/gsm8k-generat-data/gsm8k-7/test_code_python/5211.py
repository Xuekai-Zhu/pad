def solution():
    coke_parts = 2
    sprite_parts = 1
    mountain_dew_parts = 3

    coke_ounces = 6

    # Calculate the ratio of Coke to total parts
    coke_ratio = coke_parts / (coke_parts + sprite_parts + mountain_dew_parts)

    # Calculate the total number of parts in the drink
    total_parts = coke_parts + sprite_parts + mountain_dew_parts

    # Calculate the total number of ounces in the drink
    total_ounces = (coke_ounces / coke_ratio) * total_parts
    result = total_ounces
    return result

print(solution())