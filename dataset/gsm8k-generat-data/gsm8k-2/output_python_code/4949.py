def solution():
    """It takes Jerome 6 hours to run the trail around the park and it takes Nero 3 hours. If Jerome runs at 4 MPH, what speed (in MPH) does Nero run in the park?"""
    jerome_time = 6
    jerome_speed = 4
    nero_time = 3
    nero_distance = jerome_speed * jerome_time / nero_time
    nero_speed = nero_distance / nero_time
    result = nero_speed
    return result

print(solution())