def solution():
    total_miles = 70
    day_one_miles = total_miles * 0.2
    day_two_miles = (total_miles - day_one_miles) * 0.5
    day_three_miles = total_miles - (day_one_miles + day_two_miles)
    result = day_three_miles
    return result

print(solution())