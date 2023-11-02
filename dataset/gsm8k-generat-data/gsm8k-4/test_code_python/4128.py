def solution():
    """Sonia and Joss are moving to their new house at the lake. They have too much stuff in their previous house and decide to make multiple trips to move it all to the new house. They spend 15 minutes filling the car with their stuff and spend 30 minutes driving from the previous house to the new house. Fortunately, they did not waste any time unloading their stuff into the new house. In total they make 6 trips to complete the move. How many hours did they spend moving?"""
    # Define the time spent filling the car, driving, and unloading per trip
    TIME_FILLING_CAR = 15 # in minutes
    TIME_DRIVING = 30 # in minutes
    TIME_UNLOADING = 0 # in minutes as they did not waste any time unloading

    # Calculate the total time spent per trip
    total_time_per_trip = TIME_FILLING_CAR + TIME_DRIVING + TIME_UNLOADING

    # Calculate the total time spent for all trips
    total_time = total_time_per_trip * 6 # 6 trips in total

    # Convert the total time to hours
    hours = total_time / 60 # 1 hour is 60 minutes

    # Return the result
    result = hours
    return result

print(solution())