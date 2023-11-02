def solution():
    
    tank_capacity = 100
    initial_fill = tank_capacity * 2 / 5
    first_day_collect = 15
    second_day_collect = first_day_collect + 5
    total_collected = initial_fill + first_day_collect + second_day_collect
    third_day_collect = tank_capacity - total_collected
    result = third_day_collect
    return result

print(solution())