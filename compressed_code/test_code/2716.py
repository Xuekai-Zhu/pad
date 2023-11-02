def solution():
    
    bathroom_size = 24
    kitchen_size = 80
    total_size = bathroom_size + kitchen_size
    mopping_speed = 8
    total_mopping_time = total_size / mopping_speed
    result = total_mopping_time
    return result

print(solution())