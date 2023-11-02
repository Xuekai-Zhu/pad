def solution():
    """Kathryn moved to a new city for the new job she had landed two weeks ago. Her rent was $1200, 1/2 of what she spent on food and travel expenses in a month. Luckily, she found a new friend Shelby, who moved in with her to share the rent. If her salary was $5000 per month, how much money remained after her expenses?"""
    # Calculate Kathryn's food and travel expenses
    expenses = 2 * 1200  # rent is 1/2 of expenses

    # Calculate Kathryn and Shelby's total monthly expenses
    total_expenses = expenses / 2 + 1200  # split rent with Shelby

    # Calculate Kathryn's monthly savings
    monthly_savings = 5000 - total_expenses

    # Display Kathryn's monthly savings
    result = monthly_savings
    return result

print(solution())