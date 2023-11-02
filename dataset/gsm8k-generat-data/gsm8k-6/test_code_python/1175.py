def solution():
    # Calculate the cost of the t-shirt and the jeans
    sock_price = 5
    t_shirt_price = sock_price + 10  # t-shirt is $10 more expensive than the socks
    jeans_price = 2 * t_shirt_price  # jeans are twice the price of the t-shirt

    # Calculate the total cost of the t-shirt, jeans and socks
    total_cost = t_shirt_price + jeans_price + sock_price

    # Return the cost of the jeans
    result = jeans_price
    return result

print(solution())