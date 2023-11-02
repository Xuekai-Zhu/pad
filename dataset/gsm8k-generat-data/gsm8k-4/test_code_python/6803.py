def solution():
    """Kim spends $25,000 to open a store. She makes $4000 a month in revenue and her expenses are $1500 a month. How long would it take to pay back the cost to open the store?"""
    # Define the initial cost to open the store and the monthly revenue and expenses
    INITIAL_COST = 25000
    MONTHLY_REVENUE = 4000
    MONTHLY_EXPENSES = 1500

    # Calculate the profit earned each month
    MONTHLY_PROFIT = MONTHLY_REVENUE - MONTHLY_EXPENSES

    # Calculate the number of months it will take to pay back the initial cost
    months_to_payback = INITIAL_COST / MONTHLY_PROFIT

    # round up the result to the nearest whole number of months
    result = round(months_to_payback)
    return result

print(solution())