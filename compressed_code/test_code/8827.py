def solution():
    
    height = 4
    total_cases = 0
    for i in range(height):
        length = i + 1
        total_cases += length ** 2
    result = total_cases
    return result

print(solution())