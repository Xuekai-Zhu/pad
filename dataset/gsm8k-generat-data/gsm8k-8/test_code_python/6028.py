def solution():
    # Define the time she rode each day
    monday_wednesday_friday = 1
    tuesday_thursday = 0.5
    saturday = 2

    # Calculate the total time she rode in one week
    one_week_riding_time = 3*(monday_wednesday_friday) + 2*(tuesday_thursday) + saturday

    # Calculate the total time she rode in two weeks
    total_riding_time = 2 * one_week_riding_time
    result = total_riding_time
    return result

print(solution())