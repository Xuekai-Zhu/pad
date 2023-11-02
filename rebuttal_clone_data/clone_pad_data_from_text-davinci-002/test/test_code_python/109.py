def solution():
    
    run_mph = 6
    run_time_1 = 1
    run_time_2 = 0.5
    run_time_3 = 1
    run_time_4 = 0.3333333333333333
    total_run_time = run_time_1 + run_time_2 + run_time_3 + run_time_4
    total_run_miles = 20
    goal_time = total_run_miles / run_mph
    needed_time = goal_time - total_run_time
    needed_time_mins = needed_time * 60
    result = needed_time_mins
    return result

print(solution())