def solution():
    
    
    thursday_time = 50
    wednesday_time = thursday_time + 5
    tuesday_time = wednesday_time - 10
    monday_time = 2 * tuesday_time
    
    total_time = monday_time + tuesday_time + wednesday_time + thursday_time
    
    
    target_time = 5 * 60 
    friday_time = target_time - total_time
    
    result = friday_time
    return result

print(solution())