def solution():
    muffins_per_dozen = 12  # Bob orders a dozen muffins a day
    cost_per_muffin = 0.75  # Bob pays $0.75 per muffin
    selling_price_per_muffin = 1.5  # Bob sells each muffin for $1.5
    days_per_week = 7  # There are 7 days in a week

    # Calculate the cost of Bob's muffins for a week
    cost_per_week = muffins_per_dozen * cost_per_muffin * days_per_week

    # Calculate the revenue from Bob's muffins for a week
    revenue_per_week = muffins_per_dozen * selling_price_per_muffin * days_per_week

    # Calculate the profit from Bob's muffins for a week
    profit_per_week = revenue_per_week - cost_per_week
    result = profit_per_week
    return result

print(solution())