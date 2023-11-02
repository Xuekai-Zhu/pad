def solution():
    total_years = 5
    caps_per_month = 3
    increased_caps_per_month = 5
    christmas_caps = 40
    lost_caps_per_year = 15
    
    total_caps = (total_years * caps_per_month) + (total_years * increased_caps_per_month) + (total_years * christmas_caps) - (total_years * lost_caps_per_year) 
    
    result = total_caps
    
    return result

print(solution())