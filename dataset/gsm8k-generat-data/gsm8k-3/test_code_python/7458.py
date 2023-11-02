def solution():
    """Polly and Gerald went for a fun afternoon riding mini race cars at the munchkin track, which is a one-quarter mile circular track. Polly managed to circle the track 12 times in one half hour, but Gerald's car was malfunctioning, and he only moved at an average speed half of what Polly did.  What speed did Gerald's car average, in miles per hour?"""
    # Define the distance around the track
    distance = 0.25

    # Define Polly's speed
    polly_speed = distance * 12 / 0.5

    # Define Gerald's speed
    gerald_speed = polly_speed / 2

    # Convert speed to miles per hour
    gerald_speed *= 3600 / 5280

    # Display Gerald's speed
    result = gerald_speed
    return result

print(solution())