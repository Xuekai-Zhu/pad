def solution():
    """Biff and Kenneth decide to compete in a 500-yard rowboat race. If Biff rows at a speed of 50 yards per minute and Kenneth rows at a speed of 51 yards per minute, how many yards past the finish line will Kenneth be when Biff crosses the finish line?"""
    # Define the distance and speeds
    distance = 500
    biff_speed = 50
    kenneth_speed = 51

    # Calculate the time it takes for Biff to cross the finish line
    biff_time = distance / biff_speed

    # Calculate the distance Kenneth travels in the same amount of time
    kenneth_distance = kenneth_speed * biff_time

    # Calculate the distance past the finish line that Kenneth will be
    kenneth_past = kenneth_distance - distance

    # return the result
    result = kenneth_past
    return result

print(solution())