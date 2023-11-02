def solution():
    # Calculate the cost of a left-handed mouse
    left_handed_mouse_cost = 1.3 * 120

    # Calculate the daily revenue from selling left-handed mice
    daily_revenue = left_handed_mouse_cost * 25

    # Calculate the number of days in a week that Ned's store is open
    num_open_days = 7 - 3  # Ned's store is closed on Sunday, Thursday, and Friday

    # Calculate Ned's weekly revenue
    weekly_revenue = daily_revenue * num_open_days

    result = weekly_revenue
    return result

print(solution())