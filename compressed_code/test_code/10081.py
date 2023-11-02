def solution():
    
    sunday = 2
    monday = 4
    tuesday_to_friday = 3 * 4
    total_glasses = sunday + monday + tuesday_to_friday
    total_ounces = total_glasses * 10
    ounces_on_saturday = 220 - total_ounces
    glasses_on_saturday = ounces_on_saturday / 10
    result = glasses_on_saturday
    return result

print(solution())