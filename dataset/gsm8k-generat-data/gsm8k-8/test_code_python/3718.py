def solution():
    # Define the initial investment and daily operating cost
    initial_investment = 100000
    daily_operating_cost = initial_investment * 0.01

    # Calculate the daily revenue from ticket sales
    daily_revenue = 150 * 10

    # Calculate the number of days required to make back the initial investment
    days_to_break_even = initial_investment / (daily_revenue - daily_operating_cost)
    result = days_to_break_even
    return result

print(solution())