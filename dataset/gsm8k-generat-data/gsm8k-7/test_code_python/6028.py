def solution():
    hours_per_day = [1, 0.5, 1, 0.5, 1, 0, 2] # Hours per day of the week
    num_weeks = 2

    # Calculate the total hours Bethany rode in a day
    total_hours_per_day = sum(hours_per_day)

    # Calculate the total hours Bethany rode in two weeks
    total_hours = total_hours_per_day * 7 * num_weeks

    result = total_hours
    return result

print(solution())