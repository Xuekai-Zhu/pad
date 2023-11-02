def solution():
    
    total_miles = 70
    day1_miles = 0.2 * total_miles
    remaining_miles = total_miles - day1_miles
    day2_miles = 0.5 * remaining_miles
    day3_miles = total_miles - day1_miles - day2_miles
    result = day3_miles
    return result

print(solution())