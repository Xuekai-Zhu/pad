def solution():
    two_months_ago = 150  # Wilson had $150 in his bank account two months ago
    last_month_deposit = 17  # Wilson deposited $17 last month
    this_month_deposit = 21  # Wilson deposited $21 this month
    current_balance = two_months_ago + last_month_deposit - withdrawal + this_month_deposit
    # Wilson currently has $16 more than what was in his account two months ago, so we can set up an equation:
    # current_balance = two_months_ago + last_month_deposit - withdrawal + this_month_deposit + 16
    # Simplifying the equation, we get: withdrawal = two_months_ago + last_month_deposit + this_month_deposit + 16 - current_balance

    withdrawal = two_months_ago + last_month_deposit + this_month_deposit + 16 - current_balance
    result = withdrawal
    return result

print(solution())