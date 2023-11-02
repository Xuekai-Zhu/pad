def solution():
    
    monday_miles = 4
    tuesday_miles = 6 * monday_miles
    total_miles = 41
    wednesday_miles = total_miles - monday_miles - tuesday_miles
    result = wednesday_miles
    return result

print(solution())