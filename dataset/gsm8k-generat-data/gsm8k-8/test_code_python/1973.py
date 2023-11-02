def solution():
    # Define the variables
    x = 0
    friday_spending = x
    saturday_spending = 2 * x
    sunday_spending = 3 * x

    # Total spending over three days
    total_spending = friday_spending + saturday_spending + sunday_spending

    # Use the total spending equation to solve for x
    x = (120 - sunday_spending - saturday_spending) / 4

    result = x
    return result

print(solution())