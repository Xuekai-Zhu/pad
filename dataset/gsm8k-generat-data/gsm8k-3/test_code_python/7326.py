def solution():
    """Jason has a moray eel that eats 20 guppies a day and 5 betta fish who each eat 7 guppies a day. How many guppies per day does she need to buy?"""
    # Define the number of guppies each day
    moray_eel_guppies = 20
    betta_fish_guppies = 7
    num_betta_fish = 5

    # Calculate the total number of guppies needed each day
    total_guppies = moray_eel_guppies + (betta_fish_guppies * num_betta_fish)

    # Display the total number of guppies needed
    result = total_guppies
    return result

print(solution())