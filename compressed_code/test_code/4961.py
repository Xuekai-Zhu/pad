def solution():
    
    weekly_goal = 24
    daily_miles = 3
    miles_run_so_far = daily_miles * 6
    miles_left_to_run = weekly_goal - miles_run_so_far
    result = miles_left_to_run
    return result

print(solution())