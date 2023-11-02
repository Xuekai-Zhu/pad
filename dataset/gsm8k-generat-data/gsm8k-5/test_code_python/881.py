def solution():
    visits_per_week = 1  # Mark visits the theater at least once a week
    hours_per_visit = 3  # Each performance lasts 3 hours
    price_per_hour = 5  # The price of the ticket is $5 per hour
    weeks = 6  # Mark wants to know how much he will spend in 6 weeks

    # Calculate the total cost of all visits to the theater
    total_cost = visits_per_week * hours_per_visit * price_per_hour * weeks

    result = total_cost
    return result

print(solution())