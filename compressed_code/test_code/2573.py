def solution():
    
    tank_size = 50
    filling_rate = 1/20 
    filling_time = 6*60 
    total_filled = filling_rate * filling_time
    remaining_amount = tank_size - total_filled
    result = remaining_amount
    return result

print(solution())