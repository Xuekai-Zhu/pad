def solution():
    percent_spent = 0.1  # Kenneth spent 10% of his earnings
    remaining_amount = 405  # Kenneth is left with $405 after spending
    spent_amount = remaining_amount / percent_spent - remaining_amount  # Calculate the amount spent
    earnings = spent_amount + remaining_amount  # Calculate Kenneth's total earnings
    result = earnings
    return result

print(solution())