def solution():
    
    highway_miles = 210
    city_miles = 54
    highway_mpg = 35
    city_mpg = 18
    total_gallons_used = (highway_miles/highway_mpg) + (city_miles/city_mpg)
    result = total_gallons_used
    return result

print(solution())