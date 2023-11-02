def solution():
    
    goal = 3000  
    interval = 2  
    intake_per_interval = 500  
    total_intakes = goal / intake_per_interval  
    total_time = interval * total_intakes  
    result = total_time
    return result

print(solution())