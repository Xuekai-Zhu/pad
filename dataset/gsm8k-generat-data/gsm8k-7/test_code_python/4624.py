def solution():
    total_acres = 1700
    total_days = 5
    
    # Calculate the number of acres planted by two tractors in two days
    acres_planted_first = 2 * 2 * x  # Let x be the number of acres planted per tractor per day
    
    # Calculate the remaining acres to be planted
    remaining_acres = total_acres - acres_planted_first
    
    # Calculate the number of acres planted by seven tractors in three days
    acres_planted_second = 7 * 3 * x
    
    # Calculate the total acres planted
    total_acres_planted = acres_planted_first + acres_planted_second
    
    # Calculate the acres planted per tractor per day
    acres_per_tractor_per_day = total_acres_planted / (total_days * (2 + 7))
    
    result = acres_per_tractor_per_day
    return result

print(solution())