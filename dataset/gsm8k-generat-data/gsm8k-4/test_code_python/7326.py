def solution():
    """Jason has a moray eel that eats 20 guppies a day and 5 betta fish who each eat 7 guppies a day. How many guppies per day does she need to buy?"""
    # Define the number of guppies each animal eats
    moray_eel_guppies = 20
    betta_fish_guppies = 5 * 7

    # Calculate the total number of guppies needed per day
    total_guppies = moray_eel_guppies + betta_fish_guppies

    # Return the result
    result = total_guppies
    return result

print(solution())