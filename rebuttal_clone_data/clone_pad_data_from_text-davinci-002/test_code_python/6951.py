def solution():
    boxes_stored = 5000
    second_floor_storage = boxes_stored / 4
    first_floor_storage = second_floor_storage * 2
    total_storage = first_floor_storage + second_floor_storage
    available_storage = total_storage - boxes_stored
    result = available_storage
    
    return result

print(solution())