def solution():
    # Calculate the total number of minutes Noah talks to his Grammy in a year
    minutes_per_week = 30 * 2  # Noah calls his Grammy once a week for 30 minutes each time
    minutes_per_year = minutes_per_week * 52  # There are 52 weeks in a year
    # Calculate the total cost of the phone calls
    cost_per_minute = 0.05
    total_cost = cost_per_minute * minutes_per_year
    result = total_cost
    return result

print(solution())