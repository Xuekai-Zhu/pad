def solution():
    total_miles = 18
    afternoon_miles = 2 * total_miles / 3
    evening_miles = 12
    morning_miles = total_miles - afternoon_miles - evening_miles
    result = morning_miles
    return result

print(solution())