def solution():
    call_length = 30  # each call lasts 30 minutes
    rate = 0.05  # rate per minute is $0.05
    calls_per_week = 1  # Noah makes one call per week
    weeks_per_year = 52  # there are 52 weeks in a year

    # Calculate the total number of minutes Noah talks to his Grammy in a year
    total_minutes = call_length * calls_per_week * weeks_per_year

    # Calculate the total cost of the calls
    total_cost = total_minutes * rate
    result = total_cost
    return result

print(solution())