def solution():
    opening_cost = 25000  # Kim spends $25,000 to open a store
    monthly_revenue = 4000  # Kim makes $4000 a month in revenue
    monthly_expenses = 1500  # Kim's expenses are $1500 a month

    # Calculate the profit per month
    monthly_profit = monthly_revenue - monthly_expenses

    # Calculate the number of months it will take to pay back the opening cost
    months_to_pay_back = opening_cost / monthly_profit

    result = months_to_pay_back
    return result

print(solution())