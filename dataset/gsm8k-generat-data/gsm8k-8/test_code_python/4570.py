def solution():
    allowance = 12
    week1_spending = allowance / 3
    week1_balance = allowance - week1_spending
    week2_spending = week1_balance / 4
    remaining_balance = week1_balance - week2_spending
    result = remaining_balance
    return result

print(solution())