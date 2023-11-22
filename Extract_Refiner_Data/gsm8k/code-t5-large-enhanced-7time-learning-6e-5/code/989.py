def solution():
    
    # Define the number of planes and the number of trips each plane makes
    num_planes = 2
    num_trips_per_plane = 44 / 2

    # Calculate the number of flights each plane takes
    num_flights_per_plane = num_trips_per_plane / 0.25

    # Calculate the number of flights to France and Germany
    num_flights_to_france_and_gerany = num_flights_per_plane / 2

    # Calculate the number of flights to France by dividing the remaining flights equally
    num_flights_to_france = num_flights_per_plane / num_flights_per_plane

    # Display the number of flights to France by dividing the remaining flights equally
    result = num_flights_to_france
    return result

print(solution())