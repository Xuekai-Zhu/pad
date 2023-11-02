def solution():
    
    weekly_goal = 9000 * 7
    total_steps = 9400 + 9100 + 8300 + 9200 + 8900
    remaining_steps = weekly_goal - total_steps
    steps_per_day = remaining_steps / 2
    result = steps_per_day
    return result

print(solution())