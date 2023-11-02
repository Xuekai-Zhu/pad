def solution():
    
    num_units = 100
    occupancy_rate = 3/4
    rent_per_unit = 400
    total_rent_per_month = num_units * occupancy_rate * rent_per_unit
    total_rent_per_year = total_rent_per_month * 12
    result = total_rent_per_year
    return result

print(solution())