def solution():
    """James drives 30 mph for half an hour and then twice as long for twice the speed.  How far did he drive in total?"""
    # Calculate the distance covered in the first half hour
    distance1 = 30 * 0.5

    # Calculate the time and speed for the second half of the trip
    time2 = 2 * 0.5 # twice as long as the first half hour
    speed2 = 2 * 30 # twice the speed of the first half hour

    # Calculate the distance covered in the second half of the trip
    distance2 = speed2 * time2

    # Calculate the total distance covered
    total_distance = distance1 + distance2

    # Display the total distance covered
    result = total_distance
    return result

print(solution())