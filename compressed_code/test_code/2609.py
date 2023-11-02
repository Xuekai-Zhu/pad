def solution():
    
    tank_capacity = 8000
    initial_volume = 0.75 * tank_capacity
    emptied_volume = 0.4 * initial_volume
    remaining_volume = initial_volume - emptied_volume
    filled_volume = 0.3*remaining_volume
    final_volume = remaining_volume + filled_volume
    result = final_volume
    return result

print(solution())