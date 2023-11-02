def solution():
    
    starting_distance = 2
    goal_distance = 20
    
    weekly_increase = 2/3
    
    
    weeks = (goal_distance - starting_distance) / weekly_increase
    result = weeks
    
    return result

print(solution())