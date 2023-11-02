def solution():
    
    base_speed = 500
    base_capacity = 200
    additional_capacity = 100
    passenger_count = 400
    capacity_difference = (passenger_count - base_capacity) // additional_capacity
    final_speed = base_speed / (2 ** capacity_difference)
    result = final_speed
    return result

print(solution())