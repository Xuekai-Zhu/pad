def solution():
    
    num_floors = 10
    even_floor_time = 15
    odd_floor_time = 9
    total_time = 0
    
    for floor in range(1, num_floors+1):
        if floor == 1:
            total_time += odd_floor_time
        elif floor%2 == 0:
            total_time += even_floor_time
        else:
            total_time += odd_floor_time
    
    result = total_time / 60
    return result

print(solution())