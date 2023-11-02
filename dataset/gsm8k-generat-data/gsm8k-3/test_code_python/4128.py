def solution():
    """Sonia and Joss are moving to their new house at the lake. They have too much stuff in their previous house and decide to make multiple trips to move it all to the new house. They spend 15 minutes filling the car with their stuff and spend 30 minutes driving from the previous house to the new house. Fortunately, they did not waste any time unloading their stuff into the new house. In total they make 6 trips to complete the move. How many hours did they spend moving?"""
    # Define the time it takes to fill the car and drive to the new house
    FILL_AND_DRIVE_TIME = 45 # in minutes

    # Define the number of trips and the time it takes for each trip
    NUM_TRIPS = 6
    TRIP_TIME = FILL_AND_DRIVE_TIME * 2 # round-trip time

    # Calculate the total time spent moving
    total_time = (NUM_TRIPS * TRIP_TIME) / 60 # convert minutes to hours

    # Display the total time spent moving
    result = total_time
    return result

print(solution())