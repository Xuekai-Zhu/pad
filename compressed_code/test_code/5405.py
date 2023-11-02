def solution():
    
    ride_capacity = 70
    ride_duration = 20
    open_hours = 6  
    total_minutes = open_hours * 60
    total_riders = (total_minutes // ride_duration) * ride_capacity
    result = total_riders
    return result

print(solution())