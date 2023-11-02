def solution():
    """Luis is driving 80 miles in 2 hours. How far will he go in 15 minutes?"""
    # Define the distance and time taken
    distance = 80
    time_taken = 2

    # Calculate the speed
    speed = distance / time_taken

    # Calculate the distance Luis will travel in 15 minutes
    distance_in_15_min = (speed / 60) * 15

    # Round the result to the nearest tenth
    result = round(distance_in_15_min, 1)
    return result

print(solution())