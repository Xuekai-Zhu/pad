def solution():
    # Calculate the number of seats filled for each performance
    num_seats_filled = 0.8 * 400
    
    # Calculate the total revenue from each performance
    revenue_per_performance = num_seats_filled * 30
    
    # Calculate the total revenue from all three performances
    total_revenue = 3 * revenue_per_performance
    result = total_revenue
    return result

print(solution())