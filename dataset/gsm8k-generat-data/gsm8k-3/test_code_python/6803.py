def solution():
    """Kim spends $25,000 to open a store.  She makes $4000 a month in revenue and her expenses are $1500 a month.  How long would it take to pay back the cost to open the store?"""
    # Define the initial cost and monthly revenue and expenses
    initial_cost = 25000
    monthly_revenue = 4000
    monthly_expenses = 1500

    # Calculate the net profit per month
    monthly_profit = monthly_revenue - monthly_expenses

    # Calculate the number of months to pay back the initial cost
    months_to_payback = initial_cost / monthly_profit

    # Display the number of months to pay back the initial cost
    result = months_to_payback
    return result

print(solution())