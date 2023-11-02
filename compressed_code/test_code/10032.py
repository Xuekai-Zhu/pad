def solution():
    
    downhill_miles = 20
    uphill_miles = 12
    downhill_speed = 5
    uphill_speed = 3
    uphill_time = uphill_miles / uphill_speed + 1  
    downhill_time = downhill_miles / downhill_speed
    time_difference = uphill_time - downhill_time
    result = time_difference
    return result

print(solution())