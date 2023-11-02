def solution():
    
    temperatures = [40, 50, 65, 36, 82, 72, 26]
    total_temp = sum(temperatures)
    num_temp = len(temperatures)
    average_temp = total_temp / num_temp
    result = average_temp
    return result

print(solution())