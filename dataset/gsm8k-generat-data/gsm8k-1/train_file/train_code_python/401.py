def solution():
    """A new movie gets released and makes $120 million in the box office for its opening weekend. It ends up making 3.5 times that much during its entire run. If the production company gets to keep 60%, how much profit did they make if the movie cost $60 million to produce?"""
    opening_weekend_revenue = 120
    total_revenue = opening_weekend_revenue * 3.5
    production_cost = 60
    revenue_after_production_cost = total_revenue - production_cost
    profit = revenue_after_production_cost * 0.6
    result = profit
    return result

print(solution())