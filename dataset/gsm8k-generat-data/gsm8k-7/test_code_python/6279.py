def solution():
    num_large_birdhouses = 2
    large_birdhouse_price = 22

    num_medium_birdhouses = 2
    medium_birdhouse_price = 16

    num_small_birdhouses = 3
    small_birdhouse_price = 7

    # Calculate the total revenue from large birdhouses
    total_large_birdhouse_revenue = num_large_birdhouses * large_birdhouse_price

    # Calculate the total revenue from medium birdhouses
    total_medium_birdhouse_revenue = num_medium_birdhouses * medium_birdhouse_price

    # Calculate the total revenue from small birdhouses
    total_small_birdhouse_revenue = num_small_birdhouses * small_birdhouse_price

    # Calculate the total revenue from all birdhouses
    total_revenue = total_large_birdhouse_revenue + total_medium_birdhouse_revenue + total_small_birdhouse_revenue
    result = total_revenue
    return result

print(solution())