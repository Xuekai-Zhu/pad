def solution():
    """Jake makes a drink that is 2 parts Coke, 1 part Sprite and 3 parts Mountain Dew. If the drink contains 6 ounces of Coke, how many ounces is the drink?"""
    # Define the ratio of Coke, Sprite, and Mountain Dew
    coke_ratio = 2
    sprite_ratio = 1
    dew_ratio = 3

    # Calculate the total number of parts in the drink
    total_parts = coke_ratio + sprite_ratio + dew_ratio

    # Calculate the number of ounces per part of each ingredient
    coke_oz_per_part = 6 / coke_ratio
    sprite_oz_per_part = coke_oz_per_part / 2
    dew_oz_per_part = coke_oz_per_part * 1.5

    # Calculate the total number of ounces in the drink
    total_oz = (coke_oz_per_part * coke_ratio) + (sprite_oz_per_part * sprite_ratio) + (dew_oz_per_part * dew_ratio)

    # return the result
    result = total_oz
    return result

print(solution())