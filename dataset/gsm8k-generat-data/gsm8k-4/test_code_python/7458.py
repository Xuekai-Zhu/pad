def solution():
    """Polly and Gerald went for a fun afternoon riding mini race cars at the munchkin track,
     which is a one-quarter mile circular track. Polly managed to circle the track 12 times in one half hour,
     but Gerald's car was malfunctioning, and he only moved at an average speed half of what Polly did.
     What speed did Gerald's car average, in miles per hour?"""
    # Define the distance of the track
    distance = 0.25

    # Define the number of laps Polly completed and the time she took
    polly_laps = 12
    polly_time = 0.5  # in hours

    # Calculate Polly's speed
    polly_speed = (distance * polly_laps) / polly_time

    # Calculate Gerald's speed
    gerald_speed = polly_speed / 2

    # Convert the speed to miles per hour
    mph = gerald_speed * 3600 / 1609.34

    # Return the result rounded to 2 decimal places
    result = round(mph, 2)
    return result

print(solution())