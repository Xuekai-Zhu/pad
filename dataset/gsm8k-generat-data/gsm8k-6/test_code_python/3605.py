def solution():
    # Calculate the distance that Mr. Harris walked
    distance_Harris = 1  # Mr. Harris walked to a store that was 1 unit of distance away
    # Calculate the distance to your destination
    distance_destination = 3 * distance_Harris  # Your destination is 3 times further than the store Mr. Harris walked to
    # Calculate your speed
    speed = 2 * distance_Harris / 2  # You walk twice as fast as Mr. Harris
    # Calculate the time it will take you to get to your destination
    time = distance_destination / speed
    result = time
    return result

print(solution())