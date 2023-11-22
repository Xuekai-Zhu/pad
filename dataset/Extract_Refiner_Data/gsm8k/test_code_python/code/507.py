def solution():
    
    # Define the amount Gerald pays each day and the total amount spent
    DAILY_PAYMENT = 30
    TOTAL_SPENT = 100

    # Calculate the total amount Gerald spent in a week
    weekly_spending = DAILY_PAYMENT * 7

    # Calculate the amount Gerald has left
    remaining_amount = TOTAL_SPENT - weekly_spending

    # Display the amount Gerald has left
    result = remaining_amount
    return result

print(solution())