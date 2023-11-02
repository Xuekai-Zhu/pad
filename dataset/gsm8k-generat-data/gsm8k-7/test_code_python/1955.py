def solution():
    normal_mouse_cost = 120
    left_handed_mouse_cost = normal_mouse_cost * 1.3
    num_mice_sold_per_day = 25
    num_days_open_per_week = 4

    # Calculate the total revenue generated from selling left-handed mice
    total_revenue_per_day = num_mice_sold_per_day * left_handed_mouse_cost
    total_revenue_per_week = total_revenue_per_day * num_days_open_per_week

    result = total_revenue_per_week
    return result

print(solution())