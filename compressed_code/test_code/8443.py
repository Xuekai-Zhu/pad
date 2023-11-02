def solution():
    
    tank_capacity = 8000
    initial_volume = tank_capacity * (3/4)
    drained_volume = initial_volume * (40/100)
    remaining_volume = initial_volume - drained_volume
    filled_volume = remaining_volume * (30/100)
    final_volume = remaining_volume + filled_volume
    result = final_volume
    return result

print(solution())