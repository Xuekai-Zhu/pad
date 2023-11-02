def solution():
    """John drives 1000 miles a month. He needs to get an oil change every 3000 miles. He gets 1 free oil change a year. If an oil change costs $50, how much does he pay a year?"""
    total_miles_per_year = 1000 * 12
    oil_change_miles = 3000
    oil_changes_needed = total_miles_per_year // oil_change_miles
    oil_changes_needed -= 1  # subtract the free oil change
    oil_change_cost = 50
    total_cost = oil_changes_needed * oil_change_cost
    result = total_cost
    return result

print(solution())