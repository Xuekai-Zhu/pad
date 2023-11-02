def solution():
    # Define the parts of each ingredient in the drink
    coke_parts = 2
    sprite_parts = 1
    mdew_parts = 3

    # Calculate the total number of parts in the drink
    total_parts = coke_parts + sprite_parts + mdew_parts

    # Calculate the ratio of Coke to the total parts
    coke_ratio = coke_parts / total_parts

    # Calculate the total ounces of the drink
    total_ounces = 6 / coke_ratio
    result = total_ounces
    return result

print(solution())