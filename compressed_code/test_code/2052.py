def solution():
    
    charlize_time = 20
    classmates_time = [charlize_time + 10 for i in range(4)]
    total_time = charlize_time + sum(classmates_time)
    result = total_time
    return result

print(solution())