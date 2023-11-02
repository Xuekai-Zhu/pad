def solution():
    
    morning1_gallons = 68
    evening_gallons = 82
    morning2_gallons = morning1_gallons - 18
    total_gallons = morning1_gallons + evening_gallons + morning2_gallons - 24
    revenue = total_gallons * 3.5
    result = revenue
    return result

print(solution())