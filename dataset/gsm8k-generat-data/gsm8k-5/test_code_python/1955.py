def solution():
    normal_mouse_cost = 120  # Normal mice cost $120
    left_handed_mouse_cost = normal_mouse_cost * 1.3  # Left-handed mice cost 30% more than normal mice
    mice_sold_per_day = 25  # Ned sells 25 mice per day
    days_store_is_open = 7 - 3  # Ned's store is closed on Sunday, Thursday, and Friday

    # Calculate the total revenue from selling left-handed mice per week
    total_revenue_per_week = left_handed_mouse_cost * mice_sold_per_day * days_store_is_open

    # Calculate the total cost of purchasing normal mice to sell as left-handed mice
    total_cost_per_week = normal_mouse_cost * mice_sold_per_day * days_store_is_open

    # Calculate Ned's weekly profit
    weekly_profit = total_revenue_per_week - total_cost_per_week
    result = weekly_profit
    return result

print(solution())