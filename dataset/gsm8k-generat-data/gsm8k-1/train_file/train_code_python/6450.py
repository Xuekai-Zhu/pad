def solution():
    """John drives 1000 miles a month. He needs to get an oil change every 3000 miles. He gets 1 free oil change a year. If an oil change costs $50, how much does he pay a year?"""
    miles_per_month = 1000
    miles_per_year = miles_per_month * 12
    oil_change_interval = 3000
    oil_changes_needed = miles_per_year // oil_change_interval
    oil_changes_paid = oil_changes_needed - 1
    oil_change_cost = 50
    total_cost = oil_changes_paid * oil_change_cost
    result = total_cost
    
    return result

print(solution())