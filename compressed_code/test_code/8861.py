def solution():
    
    miles_per_week = 50 * 5
    gallons_per_week = miles_per_week / 25
    fill_ups_per_week = gallons_per_week / 10
    total_fill_ups = fill_ups_per_week * 4
    total_gallons = total_fill_ups * 10
    total_cost = total_gallons * 2
    result = total_cost
    return result

print(solution())