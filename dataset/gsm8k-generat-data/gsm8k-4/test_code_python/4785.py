def solution():
    """Every day, Lou works out by running three miles on a circular track that is one-quarter of a mile long. His wife, Rosie, also runs on the same track at the same time as her husband, but she runs at twice the speed of her husband. During their workout, how many times does Rosie circle the track?"""
    # Define the length of the circular track and the distance Lou runs each day
    track_length = 0.25
    lou_distance = 3

    # Calculate the number of laps Lou completes each day
    lou_laps = lou_distance / track_length

    # Calculate the speed at which Rosie runs
    rosie_speed = 2 * (lou_distance / lou_laps)

    # Calculate the number of laps Rosie completes each day
    rosie_laps = lou_laps * (rosie_speed / (2 * (lou_distance / track_length)))

    # Round the result to the nearest whole number
    result = round(rosie_laps)
    return result

print(solution())