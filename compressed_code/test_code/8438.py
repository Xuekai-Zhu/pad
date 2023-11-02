def solution():
    
    current_sodas = 48
    target_sodas = 6
    weeks = 0
    while current_sodas > target_sodas:
        current_sodas /= 2
        weeks += 1
    result = weeks
    return result

print(solution())