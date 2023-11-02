def solution():
    """TreQuan is throwing rocks in the river and he notices that the bigger the rock, the wider the splash. Pebbles make a splash that is a 1/4 meter wide. Rocks make a splash that is 1/2 a meter wide, and boulders create a splash that is 2 meters wide. If he tosses 6 pebbles, 3 rocks, and 2 boulders, what is the total width of the splashes he makes?"""
    # Define the width of each type of splash
    PEBBLE_SPLASH = 0.25
    ROCK_SPLASH = 0.5
    BOULDER_SPLASH = 2.0

    # Define the number of each type of rock thrown
    pebbles = 6
    rocks = 3
    boulders = 2

    # Calculate the total width of the splashes
    total_width = (pebbles * PEBBLE_SPLASH) + (rocks * ROCK_SPLASH) + (boulders * BOULDER_SPLASH)

    # Display the total width of the splashes
    result = total_width
    return result

print(solution())