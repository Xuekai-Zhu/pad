def solution():
    
    tank_capacity = 100
    initial_fill = tank_capacity * (2/5)
    first_day = 15
    second_day = first_day + 5
    third_day = tank_capacity - (initial_fill + first_day + second_day)
    result = third_day
    return result

print(solution())