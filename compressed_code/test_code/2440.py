def solution():
    
    goal_steps = 9000 * 7
    total_steps = 9400 + 9100 + 8300 + 9200 + 8900
    remaining_steps = goal_steps - total_steps
    remaining_days = 2
    average_needed = remaining_steps / remaining_days
    result = average_needed
    return result

print(solution())