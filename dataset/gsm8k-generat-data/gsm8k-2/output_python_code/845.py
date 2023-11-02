def solution():
    """Kurt's old refrigerator cost $0.85 a day in electricity. He recently bought a new energy-efficient refrigerator that only cost $0.45 a day in electricity. How much money does Kurt save in a 30-day month with his new refrigerator?"""
    old_refrigerator_cost_per_day = 0.85
    new_refrigerator_cost_per_day = 0.45
    days_in_month = 30
    old_refrigerator_cost_per_month = old_refrigerator_cost_per_day * days_in_month
    new_refrigerator_cost_per_month = new_refrigerator_cost_per_day * days_in_month
    cost_saved_per_month = old_refrigerator_cost_per_month - new_refrigerator_cost_per_month
    result = cost_saved_per_month
    return result

print(solution())