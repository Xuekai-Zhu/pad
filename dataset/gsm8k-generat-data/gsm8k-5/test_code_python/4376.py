def solution():
    hourly_pay = 5  # Austin receives $5 for every hour of work
    total_cost = 180  # The cost of the bicycle is $180
    hours_per_week = 2 + 1 + 3  # Austin works for a total of 6 hours per week

    # Calculate how many weeks Austin needs to work to earn enough for the bicycle
    weeks_of_work = total_cost / (hourly_pay * hours_per_week)
    result = weeks_of_work
    return result

print(solution())