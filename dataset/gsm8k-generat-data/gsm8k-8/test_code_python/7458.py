def solution():
    # Define the total distance of the track in miles
    track_distance = 0.25

    # Define the number of laps that Polly completed
    polly_laps = 12

    # Define the time it took for Polly to complete the laps in hours
    polly_time = 0.5

    # Calculate Polly's average speed in miles per hour
    polly_speed = polly_laps * track_distance / polly_time

    # Calculate Gerald's average speed, which is half of Polly's
    gerald_speed = 0.5 * polly_speed

    result = gerald_speed
    return result

print(solution())