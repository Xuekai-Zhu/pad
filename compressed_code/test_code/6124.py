def solution():
    
    total_gallons = 105
    weeks = 3
    gallons_per_week = total_gallons/weeks
    gallons_per_day = gallons_per_week/7
    current_gallon_per_day = 3
    additional_gallons = gallons_per_day - current_gallon_per_day
    result = additional_gallons
    return result

print(solution())