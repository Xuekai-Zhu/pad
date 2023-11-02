def solution():
    miles_per_month = 1000
    miles_per_oil_change = 3000
    oil_change_cost = 50
    free_oil_changes_per_year = 1

    # Calculate the total number of oil changes John needs per year
    total_miles_per_year = miles_per_month * 12
    total_oil_changes_per_year = total_miles_per_year // miles_per_oil_change
    
    # Subtract the number of free oil changes from the total number of oil changes needed
    total_paid_oil_changes = max(0, total_oil_changes_per_year - free_oil_changes_per_year)
    
    # Calculate the total cost of all paid oil changes
    total_cost = total_paid_oil_changes * oil_change_cost
    result = total_cost
    return result

print(solution())