def solution():
    """Coby went on a road trip. He is traveling from Washington to Nevada but he needs to stop in Idaho which is 640 miles away from Washington and 550 miles away from Nevada to pick up some friends.  If Coby is traveling at a speed of 80 miles per hour going to Idaho and at a speed of 50 miles per hour from Idaho to Nevada, how many hours did it take for him to arrive at the destination?"""
    # Define the distance between Washington and Idaho and the distance between Idaho and Nevada
    distance_wi = 640
    distance_in = 550

    # Define the speeds of travel between Washington and Idaho and between Idaho and Nevada
    speed_wi = 80
    speed_in = 50

    # Calculate the time it takes to travel from Washington to Idaho
    time_wi = distance_wi / speed_wi

    # Calculate the time it takes to travel from Idaho to Nevada
    time_in = distance_in / speed_in

    # Calculate the total time it takes to travel from Washington to Nevada with a stop in Idaho
    total_time = time_wi + time_in

    # Display the total time
    result = total_time
    return result

print(solution())