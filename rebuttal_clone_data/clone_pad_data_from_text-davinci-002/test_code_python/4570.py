def solution():
    allowance_per_month = 12
    allowance_per_week = allowance_per_month / 4
    spent_week_one = allowance_per_week / 3
    left_week_one = allowance_per_week - spent_week_one
    spent_week_two = left_week_one / 4
    left_week_two = left_week_one - spent_week_two
    spent_week_three = left_week_two / 3
    left_week_three = left_week_two - spent_week_three
    spent_week_four = left_week_three / 4
    left_at_end_of_month = left_week_three - spent_week_four
    result = left_at_end_of_month
    return result

print(solution())