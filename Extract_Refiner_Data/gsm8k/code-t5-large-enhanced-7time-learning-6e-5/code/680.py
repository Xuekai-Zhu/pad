def solution():
    
    # Define the total time they have to walk to school
    total_time = 30

    # Define the time it takes them to get to the corner where the library is and to get to the fire station
    library_time = 6
    fire_station_time = 13

    # Calculate the total time it takes them to get to school without being late
    total_time_without_late = total_time - library_time - fire_station_time

    # Display the time it takes them to get to school without being late
    result = total_time_without_late
    return result

print(solution())