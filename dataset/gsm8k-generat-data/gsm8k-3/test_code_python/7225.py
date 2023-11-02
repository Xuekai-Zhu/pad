def solution():
    """The Zargon Destroyer spacecraft can travel at 2 billion miles per hour in normal space, but when moving through a black hole they travel three times faster. If the Zargon Destroyer is making a voyage that travels seven hours in normal space and two hours through a black hole, how many billions of miles would they have traveled?"""
    
    # Define the speed of the Zargon Destroyer in normal space and through a black hole
    NORMAL_SPEED = 2 # billion miles per hour
    BLACKHOLE_SPEED = 3 * NORMAL_SPEED

    # Define the time spent traveling in normal space and through a black hole
    NORMAL_TIME = 7 # hours
    BLACKHOLE_TIME = 2 # hours

    # Calculate the distance traveled in normal space
    normal_distance = NORMAL_SPEED * NORMAL_TIME

    # Calculate the distance traveled through a black hole
    blackhole_distance = BLACKHOLE_SPEED * BLACKHOLE_TIME

    # Calculate the total distance traveled
    total_distance = normal_distance + blackhole_distance

    # Convert the distance traveled to billions of miles and round to 2 decimal places
    distance_in_billions = round(total_distance / 1e9, 2)

    # Display the total distance traveled in billions of miles
    result = distance_in_billions
    return result

print(solution())