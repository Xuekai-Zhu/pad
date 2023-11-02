def solution():
    # Calculate the daily running cost of the amusement park
    running_cost = 100000 * 0.01  # 1% of the initial cost

    # Calculate the daily revenue of the amusement park
    daily_revenue = 150 * 10  # 150 tickets sold a day for $10 each

    # Calculate the number of days it will take to make back the initial cost
    days_to_break_even = round((100000 + running_cost) / (daily_revenue - running_cost))

    result = days_to_break_even
    return result

print(solution())