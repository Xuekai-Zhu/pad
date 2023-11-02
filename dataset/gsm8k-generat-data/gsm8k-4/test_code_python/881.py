def solution():
    """Mark loves to see shows in theaters. He decided to visit the theater at least once a week. One performance lasts 3 hours. The price of the ticket depends on the time spent in the theater and stands at $5 for each hour. How much will Mark spend on visits to the theater in 6 weeks?"""
    # Define the number of weeks Mark will be visiting the theater
    weeks = 6

    # Define the number of visits Mark will make each week
    visits_per_week = 1

    # Define the duration of each performance in hours
    performance_duration = 3

    # Define the ticket price per hour
    ticket_price = 5

    # Calculate the total cost of all visits to the theater
    total_cost = weeks * visits_per_week * performance_duration * ticket_price

    # Return the result
    result = total_cost
    return result

print(solution())