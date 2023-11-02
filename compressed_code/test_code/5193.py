def solution():
    
    starting_lines = 24
    target_lines = 90
    lines_added_per_month = 3
    months_to_reach_target = (target_lines - starting_lines) / lines_added_per_month
    result = months_to_reach_target
    return result

print(solution())