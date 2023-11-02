def solution():
    
    total_time = 5
    current_time = 5

    for i in range(2, 6):
        current_time *= 2
        total_time += current_time

    result = total_time
    return result

print(solution())