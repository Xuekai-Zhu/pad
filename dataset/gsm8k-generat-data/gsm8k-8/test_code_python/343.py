def solution():
    # Calculate the daily electricity usage in kilowatts
    daily_usage_kwh = (125 / 1000) * 4

    # Calculate the weekly electricity usage in kilowatts
    weekly_usage_kwh = daily_usage_kwh * 7

    # Calculate the weekly electricity cost in dollars
    weekly_cost = weekly_usage_kwh * 0.14

    # Convert weekly cost to cents
    weekly_cost_cents = weekly_cost * 100

    result = weekly_cost_cents
    return result

print(solution())