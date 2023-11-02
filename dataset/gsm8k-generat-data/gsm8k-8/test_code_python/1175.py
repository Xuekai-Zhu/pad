def solution():
    # Define the cost of the socks and the relation between the t-shirt and the jeans
    sock_cost = 5
    tshirt_cost = sock_cost + 10
    jeans_cost = 2 * tshirt_cost

    # Calculate the total cost including the jeans
    total_cost = tshirt_cost + jeans_cost + sock_cost

    # Calculate the cost of the jeans alone
    jeans_alone = jeans_cost - tshirt_cost

    result = jeans_alone
    return result

print(solution())