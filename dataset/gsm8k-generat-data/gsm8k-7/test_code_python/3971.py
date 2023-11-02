def solution():
    total_miles_per_week = 30
    wednesday_miles = 12
    saturday_miles = 2 * monday_miles

    # Calculate the total number of miles Mona biked on Wednesday and Saturday
    wed_sat_miles = wednesday_miles + saturday_miles

    # Calculate the total number of miles Mona biked on Monday
    monday_miles = (total_miles_per_week - wed_sat_miles) / 3
    result = monday_miles
    return result

print(solution())