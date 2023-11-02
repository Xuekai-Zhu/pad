def solution():
    """Kurt's old refrigerator cost $0.85 a day in electricity. He recently bought a new energy-efficient refrigerator that only cost $0.45 a day in electricity. How much money does Kurt save in a 30-day month with his new refrigerator?"""
    old_cost_per_day = 0.85
    new_cost_per_day = 0.45
    days_per_month = 30
    old_cost_per_month = old_cost_per_day * days_per_month
    new_cost_per_month = new_cost_per_day * days_per_month
    savings_per_month = old_cost_per_month - new_cost_per_month
    result = savings_per_month
    return result

print(solution())