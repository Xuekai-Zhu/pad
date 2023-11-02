def solution():
    """If Amanda can run the length of a football field 2000 meters in length in 2 hours, how long would it take her to run the length of a 10000-meter track at the same speed?"""
    # Define the distance and time for the football field
    football_distance = 2000
    football_time = 2

    # Define the distance for the 10000-meter track
    track_distance = 10000

    # Calculate the time it would take to run the 10000-meter track
    track_time = (football_time / football_distance) * track_distance

    # Display the result in hours rounded to 2 decimal places
    result = round(track_time, 2)
    return result

print(solution())