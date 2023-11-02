def solution():
    """Chrystal’s vehicle speed is 30 miles per hour. Ascending the mountain decreases its speed by fifty percent, and descending the mountain increases its speed by twenty percent. If the distance going to the top of the mountain is 60 miles and the distance going down to the foot of the mountain is 72 miles, how many hours will Crystal have to pass the whole mountain?"""
    # Define Chrystal's initial speed and the distances involved
    speed = 30
    distance_up = 60
    distance_down = 72

    # Calculate Chrystal's speed while ascending the mountain and descending the mountain
    speed_up = speed / 2
    speed_down = speed * 1.2

    # Calculate the time taken by Chrystal to climb up the mountain and to come down the mountain
    time_up = distance_up / speed_up
    time_down = distance_down / speed_down

    # Calculate the total time taken by Chrystal to pass the whole mountain
    total_time = time_up + time_down

    # Display the total time
    result = total_time
    return result

print(solution())