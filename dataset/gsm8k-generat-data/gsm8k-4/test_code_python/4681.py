def solution():
    """Coby went on a road trip. He is traveling from Washington to Nevada but he needs to stop in Idaho which is 640 miles away from Washington and 550 miles away from Nevada to pick up some friends. 
    If Coby is traveling at a speed of 80 miles per hour going to Idaho and at a speed of 50 miles per hour from Idaho to Nevada, how many hours did it take for him to arrive at the destination?"""
    # Define the distances and speeds
    distance_to_idaho = 640
    distance_to_nevada = 550
    speed_to_idaho = 80
    speed_to_nevada = 50

    # Calculate the time it takes to travel to Idaho
    time_to_idaho = distance_to_idaho / speed_to_idaho

    # Calculate the time it takes to travel from Idaho to Nevada
    time_to_nevada = distance_to_nevada / speed_to_nevada

    # Calculate the total time of the trip
    total_time = time_to_idaho + time_to_nevada

    result = total_time
    return result

print(solution())