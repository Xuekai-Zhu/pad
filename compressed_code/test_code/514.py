def solution():
    
    total_engines = 5 * 80
    defective_engines = total_engines // 4
    valid_engines = total_engines - defective_engines
    result = valid_engines
    return result

print(solution())