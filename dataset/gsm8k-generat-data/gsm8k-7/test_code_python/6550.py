def solution():
    total_cars = 600
    hybrid_percentage = 0.6
    one_headlight_percentage = 0.4
    
    # Calculate the total number of hybrid cars
    total_hybrids = total_cars * hybrid_percentage
    
    # Calculate the number of hybrids with one headlight
    one_headlight_hybrids = total_hybrids * one_headlight_percentage
    
    # Calculate the number of hybrids with two headlights
    full_headlight_hybrids = total_hybrids - one_headlight_hybrids
    
    result = full_headlight_hybrids
    return result

print(solution())