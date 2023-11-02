def solution():
    monthly_allowance = 12
    spent_first_week = monthly_allowance / 3
    remaining_after_first_week = monthly_allowance - spent_first_week
    spent_second_week = remaining_after_first_week / 4
    remaining_after_second_week = remaining_after_first_week - spent_second_week
    result = remaining_after_second_week
    return result

print(solution())