def solution():
    goal_steps = 9000
    
    # Calculate the total number of steps taken so far
    total_steps = 9400 + 9100 + 8300 + 9200 + 8900
    
    # Calculate the number of steps needed on Friday and Saturday combined
    remaining_days = 2
    remaining_steps = goal_steps * remaining_days - total_steps
    
    # Calculate the average number of steps needed on Friday and Saturday
    avg_steps_needed = remaining_steps / remaining_days
    result = avg_steps_needed
    return result

print(solution())