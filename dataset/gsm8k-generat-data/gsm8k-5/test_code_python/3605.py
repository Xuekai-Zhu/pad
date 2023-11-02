def solution():
    harris_time = 2  # Mr. Harris took 2 hours to walk to the store
    your_speed = 2 * harris_speed  # You walk twice as fast as Mr. Harris
    store_distance = 1  # Mr. Harris walked to a store that is 1x away
    your_distance = 3 * store_distance  # Your destination is 3 times further away than Mr. Harris's store

    # Calculate how long it will take you to get to your destination
    your_time = your_distance / your_speed
    result = your_time
    return result

print(solution())