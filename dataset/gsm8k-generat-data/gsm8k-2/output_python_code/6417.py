def solution():
    """Macy has a goal of running a total of 24 miles per week. If she runs 3 miles per day, how many miles does Macy have left to run after 6 days so that she could meet her goal?"""
    weekly_goal = 24
    daily_miles = 3
    miles_run_so_far = daily_miles * 6
    miles_left_to_run = weekly_goal - miles_run_so_far
    result = miles_left_to_run
    return result

print(solution())