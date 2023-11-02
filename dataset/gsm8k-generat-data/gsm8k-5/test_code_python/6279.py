def solution():
    # Calculate the total revenue from large birdhouses
    revenue_large = 22 * 2  # Michael sold 2 large birdhouses for $22 each

    # Calculate the total revenue from medium birdhouses
    revenue_medium = 16 * 2  # Michael sold 2 medium birdhouses for $16 each

    # Calculate the total revenue from small birdhouses
    revenue_small = 7 * 3  # Michael sold 3 small birdhouses for $7 each

    # Calculate the total revenue from all birdhouses
    total_revenue = revenue_large + revenue_medium + revenue_small
    result = total_revenue
    return result

print(solution())