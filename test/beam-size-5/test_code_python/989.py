def solution():
    
    # Define the number of planes
    planes = 2

    # Calculate the number of flights the first plane goes to Greece
    greece_flights = planes * 0.75

    # Calculate the number of remaining flights
    remaining_flights = planes - greece_flights

    # Calculate the number of trips the first plane makes throughout each day
    trips_first_plane = 44 / 2

    # Calculate the number of flights to France the first plane takes in one day
    frights_first_plane = remaining_flights / 2

    # Display the number of flights to France
    result = frights_first_plane
    return result

print(solution())