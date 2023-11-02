def solution():
    hours_per_day = 6  # The professionals work 6 hours per day
    days = 7  # The professionals work for 7 days
    hourly_rate = 15  # One of the professionals is paid $15 per hour

    # Calculate the total hours worked by both professionals
    total_hours = 2 * hours_per_day * days

    # Calculate the total cost of hiring the professionals
    total_cost = total_hours * hourly_rate
    result = total_cost
    return result

print(solution())