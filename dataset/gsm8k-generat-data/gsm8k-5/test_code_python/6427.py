def solution():
    jury_selection_days = 2
    trial_days = 4 * jury_selection_days
    deliberation_hours = 6 * 24  # 6 full days of deliberation, 24 hours per day
    total_hours = (jury_selection_days + trial_days) * 24 + deliberation_hours
    total_days = total_hours / 16  # 16 hours per day in deliberation
    result = total_days
    return result

print(solution())