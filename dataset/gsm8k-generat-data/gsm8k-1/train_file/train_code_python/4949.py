def solution():
    """It takes Jerome 6 hours to run the trail around the park and it takes Nero 3 hours. If Jerome runs at 4 MPH, what speed (in MPH) does Nero run in the park?"""
    jerome_hours = 6
    nero_hours = 3
    jerome_speed = 4
    distance = jerome_speed * jerome_hours
    nero_speed = distance / nero_hours
    result = nero_speed
    
    return result

print(solution())