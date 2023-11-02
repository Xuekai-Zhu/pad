def solution():
    weekly_goal = 24
    days_run = 6
    miles_per_day = 3

    # Calculate the total miles run after 6 days
    total_miles_run = miles_per_day * days_run

    # Calculate the remaining miles to be run to meet the weekly goal
    remaining_miles = weekly_goal - total_miles_run
    result = remaining_miles
    return result

print(solution())