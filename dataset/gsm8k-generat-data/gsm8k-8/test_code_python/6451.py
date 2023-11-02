def solution():
    # Calculate how many oil changes John needs per year
    oil_changes_per_year = 1000 * 12 / 3000
    if oil_changes_per_year > 1:
        # Subtract 1 from the total number of oil changes if John gets 1 free per year
        oil_changes_per_year -= 1
    
    # Calculate the cost of the oil changes
    oil_change_cost = oil_changes_per_year * 50
    
    result = oil_change_cost
    return result

print(solution())