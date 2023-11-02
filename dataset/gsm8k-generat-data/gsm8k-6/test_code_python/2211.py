def solution():
    # Calculate the total miles driven in a week
    school_miles = 2 * 2 * 2.5  # round trip to school twice a day, 4 days a week
    market_miles = 2 * 2  # round trip to market once during weekends
    total_miles = school_miles + market_miles  # total miles driven in a week
    result = total_miles
    return result

print(solution())