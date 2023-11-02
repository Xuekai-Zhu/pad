def solution():
    """Christina and her friend are driving across the state. When Christina is driving the speed limit is 30 miles per hour. When her friend is driving, the speed limit is 40 miles per hour. The drive is 210 miles total. If her friend drives for 3 hours and both drive at the speed limit, how many minutes will Christina drive?"""
    # Define the total distance to be covered
    total_distance = 210

    # Define the speed limits for Christina and her friend
    christina_speed_limit = 30
    friend_speed_limit = 40

    # Define the time Christina's friend drives for
    friend_time = 3

    # Calculate the distance covered by Christina's friend
    friend_distance = friend_speed_limit * friend_time

    # Calculate the distance left to be covered after Christina's friend drives
    remaining_distance = total_distance - friend_distance

    # Calculate the time Christina will drive for to cover the remaining distance
    christina_time = remaining_distance / christina_speed_limit

    # Convert the time to minutes
    christina_time_in_minutes = christina_time * 60

    # Return the result
    result = christina_time_in_minutes
    return result

print(solution())