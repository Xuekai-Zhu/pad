def solution():
    daily_rate = 50  # Jason charges $50.00 per day
    fortnight_rate = 500  # Jason charges $500.00 for 14 days
    rental_period = 20  # Eric wants to rent the house for 20 days

    # Calculate the cost if Eric were to rent the house on a daily basis
    daily_cost = daily_rate * rental_period

    # Calculate the cost if Eric were to rent the house for 14 days and then for the remaining days separately
    fortnight_cost = fortnight_rate
    remaining_days = rental_period - 14
    remaining_cost = remaining_days * daily_rate

    # Determine the lower cost option for Eric and return the result
    if daily_cost < (fortnight_cost + remaining_cost):
        result = daily_cost
    else:
        result = fortnight_cost + remaining_cost
    return result

print(solution())