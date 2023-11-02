def solution():
    """Christina and her friend are driving across the state. When Christina is driving the speed limit is 30 miles per hour. When her friend is driving, the speed limit is 40 miles per hour. The drive is 210 miles total. If her friend drives for 3 hours and both drive at the speed limit, how many minutes will Christina drive?"""
    # Get the total distance of the drive and the friend's driving time
    total_distance = 210
    friend_time = 3

    # Calculate the remaining distance that Christina will drive
    remaining_distance = total_distance - (friend_time * 40)

    # Calculate the time Christina will drive at 30 mph (in minutes)
    christina_time = (remaining_distance / 30) * 60

    # Display the time Christina will drive
    result = christina_time
    return result

print(solution())