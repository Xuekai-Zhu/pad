def solution():
    """Kim spends $25,000 to open a store. She makes $4000 a month in revenue and her expenses are $1500 a month. How long would it take to pay back the cost to open the store?"""
    initial_cost = 25000
    monthly_profit = 4000 - 1500
    months_to_pay_back = initial_cost / monthly_profit
    result = months_to_pay_back
    
    return result

print(solution())