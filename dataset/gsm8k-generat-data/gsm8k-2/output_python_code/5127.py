def solution():
    """James pays $1000 for advertising. It brought 100 customers to his site and 80% of those bought something at the store that cost $25. How much profit does he gain from the ad?"""
    ad_cost = 1000
    customers = 100
    conversion_rate = 0.8
    profit_per_customer = 25
    total_cost = ad_cost
    total_profit = customers * conversion_rate * profit_per_customer
    net_profit = total_profit - total_cost
    result = net_profit
    return result

print(solution())