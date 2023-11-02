def solution():
    miles_per_day = 5 # Damien jogs 5 miles per day on weekdays only
    weekdays_per_week = 5 # There are 5 weekdays in a week
    weeks = 3 # Damien wants to know how many miles he will run over 3 weeks

    # Calculate the total number of miles Damien will run over 3 weeks
    total_miles = miles_per_day * weekdays_per_week * weeks

    result = total_miles
    return result

print(solution())