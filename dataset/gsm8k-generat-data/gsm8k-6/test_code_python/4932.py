def solution():
    # Calculate the total revenue from ticket sales
    revenue_tickets = 5*32 + 7*40 + 10*58  # matinee: $5, evening: $7, opening night: $10
    # Calculate the revenue from popcorn sales
    revenue_popcorn = 10 * (32+40+58) / 2  # half of the customers (total) buy popcorn for $10
    # Calculate the total revenue for the night
    total_revenue = revenue_tickets + revenue_popcorn
    result = total_revenue
    return result

print(solution())