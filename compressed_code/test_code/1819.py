def solution():
    
    mural_size = 20 * 15  
    paint_time = mural_size * 20  
    paint_time_hours = paint_time / 60
    hourly_rate = 150
    total_charge = paint_time_hours * hourly_rate
    result = total_charge
    return result

print(solution())