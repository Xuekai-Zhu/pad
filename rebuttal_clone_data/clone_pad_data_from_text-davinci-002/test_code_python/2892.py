def solution():
    total_miles = 150
    total_hours = 2
    mph_limit = 60
    avg_mph = total_miles / total_hours
    exceed_mph = avg_mph - mph_limit
    result = exceed_mph
    return result

print(solution())