def solution():
    
    # Define the time taken to hike and the speeds of the trip
    hike_time = 1.5
    trip_speed = 50

    # Calculate the distance traveled during the trip
    trip_distance = trip_speed * 6

    # Calculate the distance hiked during the trip
    hiked_distance = (trip_distance / 2) - 5

    # Calculate the total distance traveled
    total_distance = trip_distance + hiked_distance

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())