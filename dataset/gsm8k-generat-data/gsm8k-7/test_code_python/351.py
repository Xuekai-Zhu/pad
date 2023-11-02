def solution():
    weeks_of_school = 36
    missed_wednesdays = 1
    missed_fridays = 2
    sandwiches_per_week = 2

    # Calculate the total number of missed sandwich days
    missed_sandwich_days = (missed_wednesdays + missed_fridays) * sandwiches_per_week

    # Calculate the total number of sandwich days
    total_sandwich_days = (weeks_of_school * sandwiches_per_week) - missed_sandwich_days

    result = total_sandwich_days
    return result

print(solution())