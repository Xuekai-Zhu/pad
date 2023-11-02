def solution():
    # Calculate the total number of minutes in an hour
    minutes_per_hour = 60

    # Calculate the total number of minutes of talk time per customer
    talk_time = minutes_per_hour * 1

    # Calculate the cost per customer per call
    cost_per_call = talk_time * 0.05

    # Calculate the total cost for all customers in a week
    weekly_cost = cost_per_call * 50

    # Multiply the weekly cost by the number of weeks in a month to get the monthly cost
    monthly_cost = weekly_cost * 4
    result = monthly_cost
    return result

print(solution())