def solution():
    """It takes Roque two hours to walk to work and one hour to ride his bike to work. Roque walks to and from work three times a week and rides his bike to and from work twice a week. How many hours in total does he take to get to and from work a week with walking and biking?"""
    # Define the time it takes Roque to walk and ride his bike to work
    WALK_TIME = 2
    BIKE_TIME = 1

    # Define the number of times Roque walks and rides his bike to work each week
    NUM_WALKS = 3
    NUM_BIKES = 2

    # Calculate the total time Roque spends walking to and from work each week
    walk_time = WALK_TIME * 2 * NUM_WALKS

    # Calculate the total time Roque spends riding his bike to and from work each week
    bike_time = BIKE_TIME * 2 * NUM_BIKES

    # Calculate the total time Roque spends getting to and from work each week
    total_time = walk_time + bike_time

    # Return the result
    result = total_time
    return result

print(solution())