def solution():
    """Darry is a roofer and has to climb ladders multiple times a day. He climbs his full ladder, which has 11 steps, 10 times today. He also climbs his smaller ladder, which has 6 steps, 7 times today. He did not climb any steps otherwise. In total, how many times has Darry climbed a step today?"""
    # Define the number of steps on each ladder
    FULL_LADDER_STEPS = 11
    SMALL_LADDER_STEPS = 6

    # Define the number of times Darry climbed each ladder
    full_ladder_climbs = 10
    small_ladder_climbs = 7

    # Calculate the total number of steps Darry climbed
    total_steps = (FULL_LADDER_STEPS * full_ladder_climbs) + (SMALL_LADDER_STEPS * small_ladder_climbs)

    # Display the total number of steps climbed
    result = total_steps
    return result

print(solution())