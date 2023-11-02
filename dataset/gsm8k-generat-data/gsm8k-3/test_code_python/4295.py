def solution():
    """Jessica's family is 300 km away from New York. If they are traveling at the rate of 50 km/h and stop to rest for 30 minutes every 2 hours, how long will it take them to reach New York?"""
    # Define the distance to New York and the speed of the family
    distance = 300
    speed = 50

    # Calculate the time it takes to reach New York without rest stops
    time_without_rests = distance / speed

    # Calculate the number of rest stops and the time spent resting
    num_rest_stops = (time_without_rests // 2)
    time_spent_resting = num_rest_stops * 0.5

    # Calculate the total time it takes to reach New York with rest stops
    total_time = time_without_rests + time_spent_resting

    # Display the total time
    result = total_time
    return result

print(solution())