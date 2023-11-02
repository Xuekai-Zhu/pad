def solution():
    
    monday_time = 6 * 30 / 60  
    tuesday_time = 3 * 1  
    wednesday_time = 2 * tuesday_time  
    total_time = monday_time + tuesday_time + wednesday_time
    result = total_time
    return result

print(solution())