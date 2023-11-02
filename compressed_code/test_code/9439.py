def solution():
    
    total_gallons = 33
    roman_gallons = (total_gallons - 1) / 4
    remy_gallons = 3 * roman_gallons + 1
    result = remy_gallons
    return result

print(solution())