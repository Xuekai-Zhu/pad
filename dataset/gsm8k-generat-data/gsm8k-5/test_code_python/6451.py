def solution():
    miles_per_year = 1000 * 12 # John drives 1000 miles per month, so he drives 12000 miles per year
    oil_changes_needed = miles_per_year // 3000 # John needs to get an oil change every 3000 miles, so he needs oil changes for miles_per_year
    oil_changes_needed -= 1 # John gets one free oil change per year, so subtract it from oil_changes_needed
    oil_change_cost = 50 # Cost of one oil change is $50
    total_cost = oil_changes_needed * oil_change_cost # Multiply oil_changes_needed by oil_change_cost to get the total cost
    result = total_cost
    return result

print(solution())