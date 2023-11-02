def solution():
    initial_cost = 100000
    daily_cost = initial_cost * 0.01
    ticket_price = 10
    daily_revenue = ticket_price * 150

    # Calculate the number of days it takes to break even
    days_to_break_even = initial_cost / (daily_revenue - daily_cost)
    result = days_to_break_even
    return result

print(solution())