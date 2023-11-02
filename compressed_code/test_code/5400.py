def solution():
    
    tank_capacity = 4000
    fill_rate = 10
    three_fourths_capacity = 0.75 * tank_capacity
    time_to_fill = (three_fourths_capacity / fill_rate)
    result = time_to_fill
    return result

print(solution())