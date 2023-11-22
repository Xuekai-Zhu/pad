def solution():
    
    # Define the time it takes to row 20 feet of water
    shore_time = 16

    # Calculate the distance traveled towards shore
    shore_distance = 20 * shore_time

    # Calculate the amount of water taken on by the time it took to row the shore
    water_per_feet = 2 / 10
    water_taken_on = shore_distance * water_per_feet

    # Display the amount of water taken on
    result = water_taken_on
    return result

print(solution())