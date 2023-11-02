def solution():
    """Every day, Lou works out by running three miles on a circular track that is one-quarter of a mile long.  
    His wife, Rosie, also runs on the same track at the same time as her husband, but she runs at twice the speed of her husband.  
    During their workout, how many times does Rosie circle the track?"""
    # Define the length of the circular track and Lou's speed
    TRACK_LENGTH = 0.25
    LOU_SPEED = 3 / TRACK_LENGTH

    # Define Rosie's speed
    ROSIE_SPEED = 2 * LOU_SPEED

    # Calculate the time it takes Lou to run 3 miles
    lou_time = 3 / LOU_SPEED

    # Calculate the number of times Lou circles the track during his workout
    lou_circles = lou_time / (TRACK_LENGTH * 2 * math.pi)

    # Calculate the time it takes Rosie to run 3 miles
    rosie_time = 3 / ROSIE_SPEED

    # Calculate the number of times Rosie circles the track during her workout
    rosie_circles = rosie_time / (TRACK_LENGTH * 2 * math.pi)

    # Display the number of times Rosie circles the track
    result = rosie_circles
    return result

print(solution())