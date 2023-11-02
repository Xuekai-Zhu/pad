def solution():
    """Tony exercises every morning by walking 3 miles carrying a 25-pound backpack, then he runs another 10 miles without the backpack. If he walks at a speed of 3 miles per hour and runs at a speed of 5 miles per hour, how many hours each week does he spend exercising?"""
    # calculate time spent walking
    walk_distance = 3
    walk_speed = 3
    walk_time = walk_distance / walk_speed
    
    # calculate time spent running
    run_distance = 10
    run_speed = 5
    run_time = run_distance / run_speed
    
    # calculate total time spent exercising per day
    total_time = walk_time + run_time
    
    # calculate total time spent exercising per week
    days_per_week = 7
    time_per_week = total_time * days_per_week
    
    result = time_per_week
    return result

print(solution())