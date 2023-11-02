def solution():
    # Calculate the number of hours James trains in a day
    hours_per_day = 2 * 4 

    # Calculate the number of days James trains in a week
    days_per_week = 7 - 2 

    # Calculate the total number of hours James trains in a year
    hours_per_year = hours_per_day * days_per_week * 52 

    result = hours_per_year
    return result

print(solution())