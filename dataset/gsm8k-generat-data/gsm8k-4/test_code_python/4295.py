def solution():
    """Jessica's family is 300 km away from New York. If they are traveling at the rate of 50 km/h and stop to rest for 30 minutes every 2 hours, how long will it take them to reach New York?"""
    # Define the total distance to travel and the speed
    distance = 300
    speed = 50

    # Calculate the total time needed to travel without rest
    time_no_rest = distance / speed

    # Calculate the number of rest stops
    rest_stops = (time_no_rest // 2)

    # Calculate the total time needed to travel with rest stops
    time_with_rest = time_no_rest + (rest_stops * 0.5)

    # Display the total time needed to reach New York
    result = time_with_rest
    return result

print(solution())