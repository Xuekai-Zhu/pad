def solution():
    
    num_mazes = 5
    current_total_time = 45 + (4 * 50)  
    max_avg_time = 60  
    max_total_time = num_mazes * max_avg_time  

    remaining_time = max_total_time - current_total_time  
    result = remaining_time
    return result

print(solution())