def solution():
    opening_weekend_revenue = 120  # The movie made $120 million in the box office for its opening weekend
    total_revenue = 3.5 * opening_weekend_revenue  # The movie made 3.5 times that much during its entire run
    production_cost = 60  # The movie cost $60 million to produce
    revenue_after_production_costs = total_revenue - production_cost  # Calculate revenue after production costs
    profit = 0.6 * revenue_after_production_costs  # The production company gets to keep 60% of the revenue after production costs
    result = profit
    return result

print(solution())