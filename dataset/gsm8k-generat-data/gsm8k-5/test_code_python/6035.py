def solution():
    # Calculate the revenue from 5kg cargo
    revenue_5kg = 2.5 * 4  # 4 deliveries of 5kg, charged at $2.50 each

    # Calculate the revenue from 8kg cargo
    revenue_8kg = 4 * 2  # 2 deliveries of 8kg, charged at $4 each

    # Calculate the total revenue in a day
    total_revenue = revenue_5kg + revenue_8kg

    # Calculate the total revenue in a week
    total_weekly_revenue = total_revenue * 7

    result = total_weekly_revenue
    return result

print(solution())