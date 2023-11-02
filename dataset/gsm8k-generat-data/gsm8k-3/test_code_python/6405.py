def solution():
    """Tobias went to a swimming pool for 3 hours. Swimming every 100 meters took him 5 minutes, but every 25 minutes he had to take a 5-minute pause. How many meters did Tobias swim during his visit to the swimming pool?"""
    # Define the time it takes Tobias to swim 100 meters and take a break
    SWIM_TIME = 5
    BREAK_TIME = 5

    # Calculate the number of swim and break periods in 3 hours
    swim_periods = 3 * 60 // (SWIM_TIME + BREAK_TIME)

    # Calculate the total distance Tobias swam
    total_distance = swim_periods * 100

    # Display the total distance swam
    result = total_distance
    return result

print(solution())