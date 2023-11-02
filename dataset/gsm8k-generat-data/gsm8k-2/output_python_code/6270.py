def solution():
    """While on vacation in New York, Greg went out for a lunch that cost $100. If sales tax in New York is 4% and he left a 6% tip, how much did Greg pay?"""
    lunch_cost = 100
    sales_tax = 0.04 * lunch_cost
    tip = 0.06 * lunch_cost
    total_cost = lunch_cost + sales_tax + tip
    result = total_cost
    return result

print(solution())