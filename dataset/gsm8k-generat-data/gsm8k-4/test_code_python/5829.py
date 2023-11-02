def solution():
    """Tas and his friends put up a t-shirt for sale. They ended up selling 200 t-shirts in 25 minutes. Half of the shirts were black and cost $30, while the other half were white and cost $25. How much money did they make per minute during the sale?"""
    # Calculate the number of black and white shirts
    black_shirts = 100
    white_shirts = 100

    # Calculate the total revenue from black shirts
    black_revenue = black_shirts * 30

    # Calculate the total revenue from white shirts
    white_revenue = white_shirts * 25

    # Calculate the total revenue from all shirts
    total_revenue = black_revenue + white_revenue

    # Calculate the revenue per minute
    revenue_per_minute = total_revenue / 25

    result = revenue_per_minute
    return result

print(solution())