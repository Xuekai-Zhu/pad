def solution():
    """Mark loves to see shows in theaters. He decided to visit the theater at least once a week. One performance lasts 3 hours. The price of the ticket depends on the time spent in the theater and stands at $5 for each hour. How much will Mark spend on visits to the theater in 6 weeks?"""
    weekly_visits = 1
    performance_time = 3
    ticket_price = 5
    total_cost = 0
    for i in range(6):
        total_cost += weekly_visits * performance_time * ticket_price
    result = total_cost
    return result

print(solution())