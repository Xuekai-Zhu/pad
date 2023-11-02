def solution():
    # Calculate the total time spent driving to and from school per day
    time_per_day = 20 * 2 / 60 # convert to hours

    # Calculate the number of driving hours Jessica has left to complete
    hours_left = 50

    # Calculate the number of school days needed to complete the remaining driving hours
    days_needed = round(hours_left / time_per_day)

    result = days_needed
    return result

print(solution())