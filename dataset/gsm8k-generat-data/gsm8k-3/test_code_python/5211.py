def solution():
    """Jake makes a drink that is 2 parts Coke, 1 part Sprite and 3 parts Mountain Dew.  If the drink contains 6 ounces of Coke, how many ounces is the drink?"""
    # Define the ratios of each ingredient
    coke_ratio = 2
    sprite_ratio = 1
    mountain_dew_ratio = 3

    # Calculate the total number of parts
    total_ratio = coke_ratio + sprite_ratio + mountain_dew_ratio

    # Calculate the amount of each ingredient in the drink
    coke = 6
    sprite = (coke / coke_ratio) * sprite_ratio
    mountain_dew = (coke / coke_ratio) * mountain_dew_ratio

    # Calculate the total amount of the drink
    total = coke + sprite + mountain_dew

    # Display the total amount of the drink
    result = total
    return result

print(solution())