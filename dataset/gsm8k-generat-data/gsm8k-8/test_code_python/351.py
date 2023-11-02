def solution():
    # Calculate the total number of Wednesdays and Fridays in the school year
    total_days = 36 * 2
    missed_days = 1 + 2
    days_attended = total_days - missed_days

    # Calculate the number of peanut butter and jelly sandwiches eaten
    sandwiches_per_day = 1
    total_sandwiches = days_attended * sandwiches_per_day
    result = total_sandwiches
    return result

print(solution())