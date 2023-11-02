def solution():
    percent_spent = 0.1  # 10%
    remaining_amount = 405

    # Calculate the total amount Kenneth earned
    total_earnings = remaining_amount / (1 - percent_spent)
    result = total_earnings
    return result

print(solution())