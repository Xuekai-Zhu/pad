def solution():
    """TreQuan is throwing rocks in the river and he notices that the bigger the rock, the wider the splash. Pebbles make a splash that is a 1/4 meter wide. Rocks make a splash that is 1/2 a meter wide, and boulders create a splash that is 2 meters wide. If he tosses 6 pebbles, 3 rocks, and 2 boulders, what is the total width of the splashes he makes?"""
    # Define the width of the splash for each type of rock
    pebble_splash = 1/4
    rock_splash = 1/2
    boulder_splash = 2

    # Calculate the total width of the splashes
    total_splash = (6 * pebble_splash) + (3 * rock_splash) + (2 * boulder_splash)

    # Return the result
    result = total_splash
    return result

print(solution())