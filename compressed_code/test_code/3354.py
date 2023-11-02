def solution():
    
    total_units = 100
    occupied_units = total_units * 0.75
    rent_per_unit = 400
    total_rent_per_month = occupied_units * rent_per_unit
    total_rent_per_year = total_rent_per_month * 12
    result = total_rent_per_year
    return result

print(solution())