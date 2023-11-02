def solution():
    coke_parts = 2  # The drink contains 2 parts Coke
    sprite_parts = 1  # The drink contains 1 part Sprite
    mdew_parts = 3  # The drink contains 3 parts Mountain Dew
    total_parts = coke_parts + sprite_parts + mdew_parts  # The total number of parts in the drink

    # Calculate the total number of ounces in the drink
    total_ounces = (6 / coke_parts) * total_parts
    result = total_ounces
    return result

print(solution())