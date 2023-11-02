def solution():
    women_shirts_price = 18
    men_shirts_price = 15
    women_shirts_sold_per_hour = 2
    men_shirts_sold_per_hour = 1.5
    hours_per_day = 12
    days_per_week = 7

    # Calculate the total revenue from women T-shirts sold per week
    women_revenue_per_hour = women_shirts_price * women_shirts_sold_per_hour
    women_revenue_per_day = women_revenue_per_hour * hours_per_day
    total_women_revenue_per_week = women_revenue_per_day * days_per_week

    # Calculate the total revenue from men T-shirts sold per week
    men_revenue_per_hour = men_shirts_price * men_shirts_sold_per_hour
    men_revenue_per_day = men_revenue_per_hour * hours_per_day
    total_men_revenue_per_week = men_revenue_per_day * days_per_week

    # Calculate the total revenue per week
    total_revenue_per_week = total_women_revenue_per_week + total_men_revenue_per_week
    result = total_revenue_per_week
    return result

print(solution())