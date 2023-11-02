def solution():
    tank_capacity = 100
    initial_fill = 2/5
    first_day_collection = 15
    second_day_collection = first_day_collection + 5
    third_day_collection = tank_capacity - (initial_fill * tank_capacity)
    result = third_day_collection
    
    return result

print(solution())