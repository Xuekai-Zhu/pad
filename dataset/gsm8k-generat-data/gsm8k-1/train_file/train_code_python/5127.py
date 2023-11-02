def solution():
    """James pays $1000 for advertising. It brought 100 customers to his site and 80% of those bought something at the store that cost $25. How much profit does he gain from the ad?"""
    advertising_cost = 1000
    customers_brought = 100
    conversion_rate = 0.8
    purchase_amount = 25
    total_revenue = customers_brought * conversion_rate * purchase_amount
    profit = total_revenue - advertising_cost
    result = profit
    return result

print(solution())