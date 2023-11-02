def solution():
    jury_selection_days = 2
    trial_days = jury_selection_days * 4
    deliberation_hours = 6 * 24  # 6 full days of 16-hour deliberation

    total_days = jury_selection_days + trial_days + (deliberation_hours / 24)

    result = total_days
    return result

print(solution())