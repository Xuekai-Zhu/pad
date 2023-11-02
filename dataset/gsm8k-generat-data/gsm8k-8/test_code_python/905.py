def solution():
    # Number of cans produced in 1 minute
    cans_per_minute = 30

    # Number of minutes in 8 hours
    minutes_in_8_hours = 8 * 60

    # Total number of cans produced in 8 hours
    total_cans = cans_per_minute * minutes_in_8_hours

    result = total_cans
    return result

print(solution())