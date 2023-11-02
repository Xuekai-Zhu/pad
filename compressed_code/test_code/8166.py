def solution():
    
    katherine_hours_per_website = 20
    naomi_multiplier = 1.25
    naomi_hours_per_website = katherine_hours_per_website * naomi_multiplier
    
    num_websites = 30
    
    total_hours = naomi_hours_per_website * num_websites
    
    result = total_hours
    
    return result

print(solution())