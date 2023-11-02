def solution():
    """Mark loves to see shows in theaters. He decided to visit the theater at least once a week. One performance lasts 3 hours. The price of the ticket depends on the time spent in the theater and stands at $5 for each hour. How much will Mark spend on visits to the theater in 6 weeks?"""
    weeks = 6
    visits_per_week = 1
    hours_per_visit = 3
    price_per_hour = 5
    total_cost = weeks * visits_per_week * hours_per_visit * price_per_hour
    result = total_cost
    return result

print(solution())