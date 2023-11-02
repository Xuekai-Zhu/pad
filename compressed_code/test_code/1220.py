def solution():
    
    monday_time = 4
    tuesday_time = monday_time - 2
    wednesday_time = monday_time * 2
    thursday_time = tuesday_time * 2
    total_time = monday_time + tuesday_time + wednesday_time + thursday_time
    result = total_time
    return result

print(solution())