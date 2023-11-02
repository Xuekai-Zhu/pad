def solution():
    packs_per_hour_peak = 6
    packs_per_hour_low = 4
    pack_price = 60
    hours = 15

    # Calculate the total revenue during peak season
    total_revenue_peak = packs_per_hour_peak * pack_price * hours

    # Calculate the total revenue during low season
    total_revenue_low = packs_per_hour_low * pack_price * hours

    # Calculate the difference in revenue between peak season and low season
    revenue_difference = total_revenue_peak - total_revenue_low
    result = revenue_difference
    return result

print(solution())