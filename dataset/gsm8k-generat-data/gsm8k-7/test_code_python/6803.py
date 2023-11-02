def solution():
    cost = 25000
    revenue_per_month = 4000
    expenses_per_month = 1500

    # Calculate the profit per month
    profit_per_month = revenue_per_month - expenses_per_month

    # Calculate the number of months it will take to pay back the cost of opening the store
    num_months = cost / profit_per_month

    result = num_months
    return result

print(solution())