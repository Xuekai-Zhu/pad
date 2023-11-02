def solution():
    """A cheetah can run at a top speed of 60 mph.  The gazelle can run for speeds of up to 40 miles per hour.  If one mile per hour is about 1.5 feet per second, then how many seconds would it take for a cheetah traveling at top speed to catch up to a fleeing gazelle also running at top speed if the two animals were initially 210 feet apart and they both traveled in the same direction?"""
    # Define the speeds of the cheetah and gazelle in feet per second
    CHEETAH_SPEED = 60 * 1.5
    GAZELLE_SPEED = 40 * 1.5

    # Define the distance between the animals in feet
    distance = 210

    # Calculate the relative speed of the cheetah to the gazelle
    relative_speed = CHEETAH_SPEED - GAZELLE_SPEED

    # Calculate the time it takes for the cheetah to catch up to the gazelle
    time = distance / relative_speed

    # Display the time in seconds
    result = time * 3600 # convert hours to seconds
    return result

print(solution())