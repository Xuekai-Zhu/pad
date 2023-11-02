def solution():
    """Tom opens an amusement park. It cost $100,000 to open initially. It also cost 1% of that to run per day. He sells 150 tickets a day for $10 each. How long will it take to make back his money?"""
    initial_cost = 100000
    daily_cost = initial_cost * 0.01
    daily_revenue = 150 * 10
    days_to_break_even = initial_cost / (daily_revenue - daily_cost)
    result = days_to_break_even
    return result

print(solution())