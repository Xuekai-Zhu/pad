def solution():
    """Tom opens an amusement park.  It cost $100,000 to open initially.  It also cost 1% of that to run per day.  He sells 150  tickets a day for $10 each.  How long will it take to make back his money?"""
    # Define the cost to open and daily cost
    open_cost = 100000
    daily_cost = open_cost * 0.01

    # Define the revenue per day from ticket sales
    ticket_price = 10
    tickets_sold = 150
    daily_revenue = ticket_price * tickets_sold

    # Calculate the number of days to make back the initial cost
    days = open_cost / (daily_revenue - daily_cost)

    # Display the number of days
    result = days
    return result

print(solution())