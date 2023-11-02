def solution():
    
    marathon_distance = 26.3
    current_distance = 3
    months = 1
    while current_distance < marathon_distance:
        current_distance *= 2
        months += 1
    result = months
    return result

print(solution())