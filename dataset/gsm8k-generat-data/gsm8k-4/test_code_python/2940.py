def solution():
    """Chrystal’s vehicle speed is 30 miles per hour. Ascending the mountain decreases its speed by fifty percent, and descending the mountain increases its speed by twenty percent. If the distance going to the top of the mountain is 60 miles and the distance going down to the foot of the mountain is 72 miles, how many hours will Crystal have to pass the whole mountain?"""
    # Define the initial speed and the distances
    initial_speed = 30
    ascending_distance = 60
    descending_distance = 72

    # Calculate the speed when ascending the mountain
    ascending_speed = initial_speed * 0.5

    # Calculate the speed when descending the mountain
    descending_speed = initial_speed * 1.2

    # Calculate the time taken to ascend the mountain
    time_ascend = ascending_distance / ascending_speed

    # Calculate the time taken to descend the mountain
    time_descend = descending_distance / descending_speed

    # Calculate the total time taken to pass the whole mountain
    total_time = time_ascend + time_descend

    # return the result
    result = total_time
    return result

print(solution())