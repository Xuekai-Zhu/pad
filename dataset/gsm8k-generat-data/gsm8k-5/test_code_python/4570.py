def solution():
    allowance = 12  # Tom receives a $12 allowance per month

    # Calculate how much Tom spends in the first week
    week_one_spending = allowance / 3
    remaining_money = allowance - week_one_spending

    # Calculate how much Tom spends in the second week
    week_two_spending = remaining_money / 4
    remaining_money -= week_two_spending

    # Calculate how much money Tom has left to finish the month
    result = remaining_money
    return result

print(solution())