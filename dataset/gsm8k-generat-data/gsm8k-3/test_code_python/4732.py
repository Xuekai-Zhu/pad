def solution():
    """Biff and Kenneth decide to compete in a 500-yard rowboat race.  If Biff rows at a speed of 50 yards per minute and Kenneth rows at a speed of 51 yards per minute, how many yards past the finish line will Kenneth be when Biff crosses the finish line?"""
    # Define the distance of the race and the respective speeds of Biff and Kenneth
    RACE_DISTANCE = 500
    BIFF_SPEED = 50
    KENNETH_SPEED = 51

    # Calculate the time it takes for Biff to finish the race
    biff_time = RACE_DISTANCE / BIFF_SPEED

    # Calculate how far Kenneth can row in the time it takes for Biff to finish the race
    kenneth_distance = KENNETH_SPEED * biff_time

    # Calculate how far past the finish line Kenneth will be when Biff crosses the finish line
    distance_past_finish = kenneth_distance - RACE_DISTANCE

    # Display how far past the finish line Kenneth will be
    result = distance_past_finish
    return result

print(solution())