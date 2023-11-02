def solution():
    regular_complaints_per_day = 120
    increase_due_to_short_staffing = regular_complaints_per_day * (1/3)
    increase_due_to_broken_self_checkout = increase_due_to_short_staffing * 0.2
    total_complaints_per_day = regular_complaints_per_day + increase_due_to_short_staffing + increase_due_to_broken_self_checkout
    num_days = 3
    total_complaints_for_3_days = total_complaints_per_day * num_days
    result = total_complaints_for_3_days
    return result

print(solution())