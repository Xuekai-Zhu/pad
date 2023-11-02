def solution():
    """It takes Jerome 6 hours to run the trail around the park and it takes Nero 3 hours. If Jerome runs at 4 MPH, what speed (in MPH) does Nero run in the park?"""
    # Define the time and distance traveled by Jerome
    jerome_time = 6
    jerome_distance = jerome_time * 4   # speed of Jerome is given as 4 MPH

    # Calculate the speed of Nero based on the distance traveled
    nero_distance = jerome_distance
    nero_time = 3
    nero_speed = nero_distance / nero_time

    # Return the result
    result = nero_speed
    return result

print(solution())