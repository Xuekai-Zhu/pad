def solution():
    current_balance = 16
    two_months_ago = 150
    last_month = current_balance - two_months_ago + 17
    this_month = current_balance + 21
    withdrawal = last_month - this_month
    result = withdrawal
    return result

print(solution())