def solution():
    """Darry is a roofer and has to climb ladders multiple times a day. He climbs his full ladder, which has 11 steps, 10 times today. He also climbs his smaller ladder, which has 6 steps, 7 times today. He did not climb any steps otherwise. In total, how many times has Darry climbed a step today?"""
    # Define the number of steps on the full ladder and the number of times Darry climbed it
    full_ladder_steps = 11
    full_ladder_climbs = 10

    # Define the number of steps on the small ladder and the number of times Darry climbed it
    small_ladder_steps = 6
    small_ladder_climbs = 7

    # Calculate the total number of steps climbed by Darry
    total_steps_climbed = full_ladder_steps * full_ladder_climbs + small_ladder_steps * small_ladder_climbs

    # Return the result
    result = total_steps_climbed
    return result

print(solution())