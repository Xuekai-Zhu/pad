def solution():
    
    plantation_area = 500 * 500
    peanut_production = plantation_area * 50
    peanut_butter_production = peanut_production / 20 * 5
    peanut_butter_in_kg = peanut_butter_production / 1000
    profit = peanut_butter_in_kg * 10
    result = profit
    return result

print(solution())