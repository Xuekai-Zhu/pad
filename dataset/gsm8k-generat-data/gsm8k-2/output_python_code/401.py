def solution():
    """A new movie gets released and makes $120 million in the box office for its opening weekend. It ends up making 3.5 times that much during its entire run. If the production company gets to keep 60%, how much profit did they make if the movie cost $60 million to produce?"""
    opening_weekend_revenue = 120
    total_revenue = opening_weekend_revenue * 3.5
    production_cost = 60
    net_profit = (total_revenue * 0.6) - production_cost
    result = net_profit
    return result

print(solution())