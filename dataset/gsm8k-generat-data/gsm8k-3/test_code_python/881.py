def solution():
    """Mark loves to see shows in theaters. He decided to visit the theater at least once a week. One performance lasts 3 hours. The price of the ticket depends on the time spent in the theater and stands at $5 for each hour. How much will Mark spend on visits to the theater in 6 weeks?"""
    # Define the duration of one performance and the ticket price per hour
    duration = 3
    price_per_hour = 5

    # Calculate the total cost for 6 weeks of theater visits
    weeks = 6
    total_cost = 0
    for i in range(weeks):
        total_cost += duration * price_per_hour
    result = total_cost
    return result

print(solution())