def solution():
    # Check if the presence of a crucifix is likely in Karachi
    is_christian_symbol_present = False
    karachi_population_is_muslim = True
    
    if is_christian_symbol_present and not karachi_population_is_muslim:
        result = "yes"
    else:
        result = "no"
        
    return result

print(solution())