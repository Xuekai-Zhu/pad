def solution():
    allowance = 12  # $12 allowance per month
    spent_first_week = allowance / 3  # Tom spends a third of his allowance in the first week
    remaining_second_week = allowance - spent_first_week  # Tom has this much money left for the second week
    spent_second_week = remaining_second_week / 4  # Tom spends a quarter of what he has left in the second week
    remaining_balance = allowance - spent_first_week - spent_second_week  # Tom's remaining balance for the month
    result = remaining_balance
    return result

print(solution())