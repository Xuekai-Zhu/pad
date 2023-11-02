def solution():
    
    jury_selection_days = 2
    trial_days = jury_selection_days * 4
    deliberation_hours = 6 * 24
    deliberation_days = deliberation_hours / 16
    total_days = jury_selection_days + trial_days + deliberation_days
    result = total_days
    return result

print(solution())