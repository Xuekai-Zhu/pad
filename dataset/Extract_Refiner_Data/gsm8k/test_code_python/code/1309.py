def solution():
    
    # Define the number of watermelons and the cost of each watermelon
    num_watermelons = 50
    cost_per_watermelon = 80 / num_watermelons

    # Calculate the total revenue from selling all the watermelons
    total_revenue = cost_per_watermelon * 1.25

    # Calculate the revenue per watermelon sold
    revenue_per_watermelon = total_revenue / num_watermelons

    # Display the revenue per watermelon sold
    result = revenue_per_watermelon
    return result

print(solution())