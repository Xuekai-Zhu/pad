def solution():
    # Find the number of 2-hour intervals from 3 A.M. to 11 A.M.
    hours_passed = 8
    intervals_passed = hours_passed // 2

    # Find the total increase in temperature over those intervals
    increase_per_interval = 1.5
    total_increase = increase_per_interval * intervals_passed

    # Add the increase to the starting temperature of 50 degrees
    starting_temp = 50
    final_temp = starting_temp + total_increase

    result = final_temp
    return result

print(solution())