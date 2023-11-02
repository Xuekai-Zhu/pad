def solution():
    """Macy has a goal of running a total of 24 miles per week. If she runs 3 miles per day, how many miles does Macy have left to run after 6 days so that she could meet her goal?"""
    weekly_goal = 24
    miles_per_day = 3
    miles_run = miles_per_day * 6
    miles_left = weekly_goal - miles_run
    result = miles_left
    return result

print(solution())