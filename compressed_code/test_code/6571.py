def solution():
    
    ounces_per_bowl = 10
    bowls_per_minute = 5
    ounces_per_gallon = 128
    gallons_of_soup = 6
    
    total_ounces = gallons_of_soup * ounces_per_gallon
    total_bowls = total_ounces / ounces_per_bowl
    minutes = total_bowls / bowls_per_minute
    
    result = round(minutes)
    return result

print(solution())