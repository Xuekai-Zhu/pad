def solution():
    """While on vacation in New York, Greg went out for a lunch that cost $100. If sales tax in New York is 4% and he left a 6% tip, how much did Greg pay?"""
    meal_cost = 100
    sales_tax = 0.04
    tip_percent = 0.06
    tax_amount = meal_cost * sales_tax
    tip_amount = meal_cost * tip_percent
    total_cost = meal_cost + tax_amount + tip_amount
    result = total_cost
    return result

print(solution())