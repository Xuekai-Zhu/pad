def solution():
    """Sol sells candy bars to raise money for her softball team. On the first day, she sells ten candy bars and sells four more candy bars than she sold the previous day each day afterward. If she sells six days a week and each candy bar costs 10 cents, how much will she earn in a week in dollars?"""
    starting_sales = 10
    daily_sales_increase = 4
    total_sales = starting_sales
    
    for i in range(5):
        total_sales += starting_sales + (i + 1) * daily_sales_increase
    
    total_earnings = total_sales * 0.10 * 6 # assuming each candy bar costs 10 cents
    
    result = round(total_earnings, 2)
    return result

print(solution())