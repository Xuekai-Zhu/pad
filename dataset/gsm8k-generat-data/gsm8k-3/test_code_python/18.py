def solution():
    """It takes Roque two hours to walk to work and one hour to ride his bike to work. Roque walks to and from work three times a week and rides his bike to and from work twice a week. How many hours in total does he take to get to and from work a week with walking and biking?"""
    # Define the time it takes Roque to walk and ride his bike to work
    WALK_TIME = 2
    BIKE_TIME = 1

    # Define the number of times Roque walks and rides his bike to work each week
    WALK_FREQUENCY = 3
    BIKE_FREQUENCY = 2

    # Calculate the total time Roque takes to walk to and from work in a week
    total_walk_time = WALK_FREQUENCY * (2 * WALK_TIME)

    # Calculate the total time Roque takes to ride his bike to and from work in a week
    total_bike_time = BIKE_FREQUENCY * (2 * BIKE_TIME)

    # Calculate the total time Roque takes to get to and from work in a week
    total_time = total_walk_time + total_bike_time

    # Return the result
    result = total_time
    return result

print(solution())