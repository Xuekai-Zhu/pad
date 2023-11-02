def solution():
    initial_cost = 100000  # The cost to open the amusement park
    daily_cost = initial_cost * 0.01  # The cost to run the amusement park per day
    daily_revenue = 150 * 10  # The revenue generated per day from selling tickets

    # Calculate the number of days it will take to make back the initial cost
    days_to_break_even = initial_cost / (daily_revenue - daily_cost)
    result = days_to_break_even
    return result

print(solution())