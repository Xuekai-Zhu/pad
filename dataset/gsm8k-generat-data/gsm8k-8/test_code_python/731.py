def solution():
    # Define the number of shirts and jeans
    num_shirts = 20
    num_jeans = 10

    # Define the cost of a shirt and double it for a pair of jeans
    shirt_cost = 10
    jeans_cost = 2 * shirt_cost

    # Calculate the total revenue from selling all the shirts and jeans
    total_revenue = num_shirts * shirt_cost + num_jeans * jeans_cost
    result = total_revenue
    return result

print(solution())