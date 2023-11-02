def solution():
    jury_selection = 2
    trial_length = jury_selection * 4
    deliberation_length = 6
    hours_per_day = 16
    total_hours = jury_selection + trial_length + (deliberation_length * hours_per_day)
    days = total_hours / hours_per_day
    result = days
    return result

print(solution())