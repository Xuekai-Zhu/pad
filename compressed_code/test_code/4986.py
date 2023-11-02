def solution():
    
    total_miles_per_year = 1000 * 12
    oil_change_miles = 3000
    oil_changes_needed = total_miles_per_year // oil_change_miles
    oil_changes_needed -= 1  
    oil_change_cost = 50
    total_cost = oil_changes_needed * oil_change_cost
    result = total_cost
    return result

print(solution())