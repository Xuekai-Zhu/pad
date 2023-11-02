def solution():
    
    even_floor_time = 15
    odd_floor_time = 9
    total_floors = 10
    total_time = 0
    for i in range(1, total_floors + 1):
        if i % 2 == 0:
            total_time += even_floor_time
        else:
            total_time += odd_floor_time
    total_time /= 60 
    result = total_time
    return result

print(solution())